# Imports
from django.shortcuts import render
from django.http import JsonResponse
from .services.google_books import book_search

def book_search_view(request):
    """
    View for the search results
        * Checks if there’s a search query from the user
        * If there is a query, it calls book_search() to fetch the data.
        * It returns a list of books with their corresponding title, author, cover image, and genre (if available)
        * Passes the result to the book_search.html template to display it.
    """
    query = request.GET.get('q', '')
    books = []  # This will hold the processed book information
    posts = []  # Presumably you'll populate this with related posts

    if query:
        # Call the book_search function to get the raw results
        results = book_search(query)

        # Process each book item and append to the books list
        for book in results:  # results should be a list now
            volume_info = book.get('volumeInfo', {})
            book_info = {
                'id': book.get('id'),
                'title': volume_info.get('title', 'Title not available'),
                'author': volume_info.get('authors', ['Author not available']),
                'cover_image': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                'genre': volume_info.get('categories', ['Genre not available']),
            }
            books.append(book_info)

    # Checks if it's an AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Returns JSON response for AJAX
        return JsonResponse(books, safe=False)
    
    # Otherwise, renders the results in the search template
    return render(request, 'books/general_search.html', {
        'books': books,
        'posts': posts,
        'query': query
    })
