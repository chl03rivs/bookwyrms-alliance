# Imports
from django import forms
from django_summernote.widgets import SummernoteWidget
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
        fields = ('post_title', 'category', 'body') # add 'book' later
        widgets = {
            'body': SummernoteWidget(),
        }