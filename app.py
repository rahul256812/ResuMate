from flask import Flask, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret in production

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['resume_builder']
users_col = db['users']

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Auth page
@app.route('/auth')
def auth():
    form = request.args.get('form', 'signin')
    return render_template('auth.html', form=form)

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm = request.form['confirm_password']

    if password != confirm:
        return "Passwords do not match"

    existing_user = users_col.find_one({'email': email})
    if existing_user:
        return "Email already exists"

    hashed_pw = generate_password_hash(password)
    users_col.insert_one({
        'username': username,
        'email': email,
        'password': hashed_pw
    })

    session['user'] = {'username': username, 'email': email}
    return redirect(url_for('home'))

# Login route
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    user = users_col.find_one({'email': email})
    if user and check_password_hash(user['password'], password):
        session['user'] = {'username': user['username'], 'email': user['email']}
        return redirect(url_for('home'))
    else:
        return "Invalid credentials"

# Logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

# Dashboard placeholder (resume builder)
@app.route('/dashboard')
def dashboard():
    if not session.get('user'):
        return redirect(url_for('auth') + '?form=signin')
    return render_template('dashboard.html')

from bson.objectid import ObjectId

@app.route('/save_resume', methods=['POST'])
def save_resume():
    if 'user' not in session:
        return redirect(url_for('auth') + '?form=signin')

    form = request.form.to_dict(flat=False)

    resume_data = {
        'user_email': session['user']['email'],
        'name': form.get('name', [''])[0],
        'email': form.get('email', [''])[0],
        'phone': form.get('phone', [''])[0],
        'location': form.get('location', [''])[0],
        'website': form.get('website', [''])[0],
        'github': form.get('github', [''])[0],
        'linkedin': form.get('linkedin', [''])[0],
        'summary': form.get('summary', [''])[0],
        'skills': [s.strip() for s in form.get('skills', [''])[0].split(',')],
        'education': [],
        'experience': [],
        'projects': []
    }

    # Handle dynamic education
    for key in form:
        if key.startswith('education'):
            parts = key.split('[')
            index = int(parts[1][:-1])
            field = parts[2][:-1]
            while len(resume_data['education']) <= index:
                resume_data['education'].append({})
            resume_data['education'][index][field] = form[key][0]

    # Handle dynamic experience
    for key in form:
        if key.startswith('experience'):
            parts = key.split('[')
            index = int(parts[1][:-1])
            field = parts[2][:-1]
            while len(resume_data['experience']) <= index:
                resume_data['experience'].append({})
            resume_data['experience'][index][field] = form[key][0]

    # Handle dynamic projects
    for key in form:
        if key.startswith('projects'):
            parts = key.split('[')
            index = int(parts[1][:-1])
            field = parts[2][:-1]
            while len(resume_data['projects']) <= index:
                resume_data['projects'].append({})
            resume_data['projects'][index][field] = form[key][0]

    # Insert into MongoDB
    result = db.resumes.insert_one(resume_data)
    resume_id = str(result.inserted_id)

    # Redirect to preview
    return redirect(url_for('view_resume', resume_id=resume_id))



@app.route('/resume/<resume_id>')
def view_resume(resume_id):
    resume = db.resumes.find_one({'_id': ObjectId(resume_id)})
    if not resume:
        return "Resume not found", 404

    return render_template('resume.html', resume=resume)



if __name__ == '__main__':
    app.run(debug=True)