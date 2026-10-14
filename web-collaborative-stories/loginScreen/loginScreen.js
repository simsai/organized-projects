document.addEventListener('DOMContentLoaded', function() {
    // Get the submit button element
    const signInBtn = document.getElementById('signInBtn');

    // Add click event listener
    signInBtn.addEventListener('click', function() {
        // Redirect to index.html
        window.location.href = '../index.html';
    });
});
