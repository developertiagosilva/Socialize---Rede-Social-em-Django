# posts/forms.py

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': '3',
            'placeholder': 'No que você está pensando agora?'
        }),
        label=""
    )

    class Meta:
        model = Post
        fields = ['content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-sm',
            'placeholder': 'Escreva um comentário ou resposta...'
        }),
        label=""
    )

    class Meta:
        model = Comment
        fields = ['content']