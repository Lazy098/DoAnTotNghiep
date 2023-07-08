// Function to show the edit form
function showEditForm(postId) {
    // Show the edit form for the specific post
    var formId = 'user-edit-form-' + postId;
    document.getElementById(formId).style.display = 'block';
}

// Function to hide the edit form for a specific post
function hideEditForm(postId) {
    // Hide the edit form for the specific post
    var formId = 'user-edit-form-' + postId;
    document.getElementById(formId).style.display = 'none';
}

// Add event listener to the "Edit Post" buttons
var editButtons = document.getElementsByClassName('user-edit-form');
for (var i = 0; i < editButtons.length; i++) {
    editButtons[i].addEventListener('click', function() {
        var postId = this.getAttribute('data-id');
        showEditForm(postId);
    });
}

// Add event listener to the "Close" button of each edit form
var closeButtons = document.getElementsByClassName('user-edit-close');
for (var i = 0; i < closeButtons.length; i++) {
    closeButtons[i].addEventListener('click', function() {
        var postId = this.getAttribute('data-id');
        hideEditForm(postId);
    });
}