// AJAX Search feature for inline results
document.getElementById('book-search').addEventListener('input', function() {
    var query = this.value;
    if (query.length > 2) {  // Wait for at least 3 characters
        fetch(`/your-books-search-url?q=${query}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'  // For AJAX detection
            }
        })
        .then(response => response.json())
        .then(data => {
            var resultsDiv = document.getElementById('search-results');
            resultsDiv.innerHTML = '';  // Clears previous results

            // Loops through the results and create a list or pop-out view
            data.forEach(book => {
                var bookElement = document.createElement('div');
                bookElement.classList.add('book-item');
                bookElement.innerHTML = `
                    <strong>${book.title}</strong> by ${book.authors.join(', ')}
                    <img src="${book.cover_image}" alt="Cover Image" />
                    <p>Genres: ${book.genres.join(', ')}</p>
                `;
                resultsDiv.appendChild(bookElement);

                // Click event to select the book
                bookElement.addEventListener('click', function() {
                    // Handle the book selection and add it to the form
                });
            });
        });
    }
});
