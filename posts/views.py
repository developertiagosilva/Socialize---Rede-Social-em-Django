# posts/views.py

from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm

@login_required
def add_comment_view(request, post_id):
    """Adiciona um comentário num post ou responde a outro comentário"""
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.profile

            # Se for uma resposta a outro comentário (Comentário do Comentário)
            parent_id = request.POST.get('parent_id')
            if parent_id:
                parent_comment = get_object_or_404(Comment, id=parent_id)
                comment.parent = parent_comment

            comment.save()
            messages.success(request, "Comentário enviado!")

    return redirect('home')


@login_required
def like_comment_view(request, comment_id):
    """Curte ou descurte um comentário"""
    comment = get_object_or_404(Comment, id=comment_id)
    profile = request.user.profile

    # Lógica de Toggle (Se já curtiu, descurte. Se não curtiu, curte)
    if profile in comment.likes.all():
        comment.likes.remove(profile)
    else:
        comment.likes.add(profile)

    return redirect('home')


@login_required
def like_post_view(request, post_id):
    """Curte ou descurte um post principal"""
    post = get_object_or_404(Post, id=post_id)
    profile = request.user.profile

    if profile in post.likes.all():
        post.likes.remove(profile)
    else:
        post.likes.add(profile)

    return redirect('home')