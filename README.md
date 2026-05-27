# Resumate - AI Resume Builder 🚀

Resumate is a modern, high-fidelity web application built with Python Flask and MongoDB. It features a premium, responsive glassmorphic UI and empowers users to construct, organize, and instantly export professional resume profiles into print-ready A4 PDF documents.

---

## ✨ Features

*   **Premium Glassmorphic Design:** Sleek typography (Outfit & Inter), harmony-focused color palettes, subtle micro-interactions, and floating animated visual blobs.
*   **Secure Authentication System:** Session-based user sign-up and login with password cryptographic hashing via `werkzeug.security`.
*   **Interactive Dynamic Builder:** Add multiple education milestones, career experiences, and custom projects on the fly with a dynamic client-side DOM injector.
*   **Smart Skills Parser:** Automatically converts comma-separated inputs into clean, visual tag badges on the generated document.
*   **Direct PDF Engine:** Export clean, perfectly styled, and A4 print-optimized documents directly to local storage using `html2pdf.js`.

---

## 🛠️ Tech Stack

*   **Backend:** Python 3.x, Flask (v3.0.0)
*   **Database:** MongoDB (using `pymongo` driver)
*   **Frontend:** Semantic HTML5, Vanilla JavaScript, and Custom Modern CSS

---

## 📂 Folder Structure

```text
resume-builder/
├── app.py                  # Core Flask controller & API routes
├── requirements.txt        # Backend dependencies
├── static/
│   ├── css/
│   │   ├── index.css       # Home page styles
│   │   ├── auth.css        # Authentication layout styles
│   │   ├── dashboard.css   # Dynamic builder styles
│   │   └── resume.css      # Print & digital A4 resume document styling
│   └── js/
│       └── auth.js         # Slide-switching container behaviors
└── templates/
    ├── index.html          # Dynamic landing page view
    ├── auth.html           # Dual signup/login dynamic view
    ├── dashboard.html      # Interactive resume form view
    └── resume.html         # Live print preview and export engine view
```

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have the following installed on your system:
*   [Python 3.8+](https://www.python.org/downloads/)
*   [MongoDB Community Server](https://www.mongodb.com/docs/manual/administration/install-community/) (running locally on standard port `27017`)

### 2. Installation
Clone or navigate to the repository directory and set up a virtual environment:

```bash
# Initialize a virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 3. Running the Server
Make sure your MongoDB server is up and running. Then, execute:

```bash
python app.py
```

Open your browser and navigate to `http://127.0.0.1:5000` to start building your resumes!

---

## 📄 License
This project is open-source and available under the MIT License.
