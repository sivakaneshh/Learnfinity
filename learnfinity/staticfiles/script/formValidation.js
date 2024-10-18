document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const emailInput = document.querySelector('input[name="username"]');
    const passwordInput = document.querySelector('input[name="password"]');
    
    form.addEventListener("submit", function(event) {
      if (emailInput.value === "" || passwordInput.value === "") {
        event.preventDefault();
        alert("Please fill out both the email and password fields.");
      }
    });
  });
  