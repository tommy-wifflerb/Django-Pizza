from django import forms
from .models import Pizza, Topping, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': 'Comment:'}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}