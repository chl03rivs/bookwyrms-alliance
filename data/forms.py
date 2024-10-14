# Imports
from django import forms
from django_summernote.widgets import SummernoteWidget

from books.services.google_books import book_search
from .models import Comment, Post

# Inherited from built-in Django classes
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'body': SummernoteWidget(),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'book_author', 'book_title', 'book_genre', 'category', 'body')
        widgets = {
            'body': SummernoteWidget(),
        }