from .models import Comment
from django import forms

# Comment form class
# Inherited from a built-in Django class
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)