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
    
    # Adicionando o campo de imagem de forma opcional
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        }),
        label="Adicionar Imagem"
    )

    class Meta:
        model = Post
        fields = ['content', 'image']


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