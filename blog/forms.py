from .models import Comment
from django import forms

# Form for handling comments in the blog applications.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
