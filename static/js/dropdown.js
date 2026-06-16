/* ResuMate User Menu Dropdown Functionality */

function toggleUserDropdown(event) {
  event.preventDefault();
  event.stopPropagation();
  const menu = document.getElementById('userDropdownMenu');
  if (menu) {
    menu.classList.toggle('show');
  }
}

// Close the dropdown if the user clicks anywhere outside of it
document.addEventListener('click', function(event) {
  const menu = document.getElementById('userDropdownMenu');
  const trigger = document.querySelector('.dropdown-trigger');
  
  if (menu && menu.classList.contains('show')) {
    // If the click was not inside the menu and not on the trigger
    if (!menu.contains(event.target) && (!trigger || !trigger.contains(event.target))) {
      menu.classList.remove('show');
    }
  }
});
