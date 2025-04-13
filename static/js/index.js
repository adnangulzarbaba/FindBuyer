// script.js

// Show a message when the user selects a file
const fileInput = document.querySelector('.file-input');
if (fileInput) {
  fileInput.addEventListener('change', function() {
    if (this.files.length > 0) {
      alert(`Selected file: ${this.files[0].name}`);
    }
  });
}

// Confirm before submitting if "Send emails automatically" is checked
const form = document.querySelector('form');
if (form) {
  form.addEventListener('submit', function(event) {
    const sendEmailsCheckbox = document.querySelector('input[name="send_emails"]');
    if (sendEmailsCheckbox && sendEmailsCheckbox.checked) {
      const confirmSend = confirm("Are you sure you want to send emails automatically?");
      if (!confirmSend) {
        event.preventDefault(); // Cancel form submission
      }
    }
  });
}
