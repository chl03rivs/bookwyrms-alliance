import requests
from django.conf import settings

GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'

def book_search(query):
    """
    Service that interacts with the Google Books API
        * Sends a request to the API with the user’s search query and the API key.
        * If the request succeeds, it returns a list of books from the API response. 
        * Otherwise, it catches errors and returns an empty list.
    """
    params = {
        'q': query,
        'key': settings.GOOGLE_BOOKS_API_KEY,  # Safely pulls the API key from environment settings
        'maxResults': 5  # Limits the number of results returned
    }
    
    try:
        response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
        
        # Checks if the response status is 200 (OK)
        if response.status_code == 200:
            # Returns 'items' (list of books) or an empty list if not found
            return response.json().get('items', [])
        else:
            print(f"Failed to retrieve books. Status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        # Catches any errors that occur during the request (e.g., network issues)
        print(f"Error fetching data from Google Books API: {e}")
        return [] 