# posts/urls.py

from django.urls import path
from . import views
from .views import like_post_view

urlpatterns = [
    path('comment/<int:post_id>/', views.add_comment_view, name='add_comment'),
    path('like-comment/<int:comment_id>/', views.like_comment_view, name='like_comment'),
    path('like-post/<int:post_id>/', views.like_post_view, name='like_post'),  # <-- NOVA ROTA
    path('like/<int:post_id>/', like_post_view, name='like_post'),
]