# posts/urls.py

from django.urls import path
from . import views
from .views import like_post_view, excluir_post, add_comment_view, like_comment_view

urlpatterns = [
    path('comment/<int:post_id>/', add_comment_view, name='add_comment'),
    path('like-comment/<int:comment_id>/', like_comment_view, name='like_comment'),
    path('like/<int:post_id>/', like_post_view, name='like_post'),
    path('post/excluir/<int:pk>/', excluir_post, name='excluir_post'),
]