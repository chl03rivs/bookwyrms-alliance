from .models import Comment
from django import forms

# Inherited from built-in Django classes
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'body', 'category')