// Data app scripts

// COMMENTS
function editComment(commentId) {
    document.getElementById(`edit-comment-form-${commentId}`).style.display = 'block'; // Display hidden form
}
// Saves the changes via AJAX
function saveComment(commentId, postSlug) {
    const newContent = document.getElementById(`edit-comment-content-${commentId}`).value;

    fetch(`/post/${postSlug}/comment/${commentId}/edit/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            // CSRF token must be included
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({ content: newContent })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Update the comment content on the page
            document.querySelector(`#comment-${commentId} p`).innerText = newContent;
            cancelEdit(commentId);  // Hide the edit form
        } else {
            alert('Failed to update comment.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error updating comment.');
    });
}
// POSTS

// Functions common to posts and comments
// Validation
function validateContent(content) {
    if (!content.trim()) {
        alert('Content cannot be empty.');
        return false;
    }
    return true;
}
// Error handling
function handleSaveError(error) {
    console.error('Save Error:', error);
    alert('An error occurred while saving. Please try again.');
}

// Cancels edits
function cancelEdit(type, id) {
    // Get the edit form for the specific post or comment
    const editForm = document.getElementById(`edit-${type}-form-${id}`);
    // Get the original content to display again
    const content = document.getElementById(`${type}-content-${id}`);
    // Hide the edit form
    if (editForm) {
        editForm.style.display = 'none';
    }
    // Show the original content again
    if (content) {
        content.style.display = 'block';
    }
}
// Deletes content
function deleteContent(type, id) {
    if (confirm(`Delete this ${type}? This cannot be undone.`)) {
        // Performs the delete operation (AJAX request)
        console.log(`Deleting ${type} with ID ${id}`);
        
        // If delete is successful, removes the element from the DOM
        const element = document.getElementById(`${type}-${id}`);
        if (element) {
            element.remove();
        }
    }
}

// Function that gets the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Initialization Functions
function initializeCommentScripts() {
    document.querySelectorAll('.edit-comment-btn').forEach(button => {
        const commentId = button.dataset.commentId;
        button.addEventListener('click', () => editComment(commentId));
    });
    

}
function initializePostScripts() {
    document.querySelectorAll('.edit-post-btn').forEach(button => {
        const postId = button.dataset.postIdId;
        button.addEventListener('click', () => editPost(postId));
    });
    

}

document.addEventListener('DOMContentLoaded', function() {
    initializeCommentScripts();
    initializePostScripts();
});