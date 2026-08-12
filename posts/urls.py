# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('comment/<int:post_id>/', views.add_comment_view, name='add_comment'),
    path('like-comment/<int:comment_id>/', views.like_comment_view, name='like_comment'),
    path('like-post/<int:post_id>/', views.like_post_view, name='like_post'),  # <-- NOVA ROTA
]