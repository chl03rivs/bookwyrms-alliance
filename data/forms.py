# Imports
from django import forms

from .models import Comment, Post

# Inherited from built-in Django classes
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body', 'category')