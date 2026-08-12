
from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at', 'content_preview')
    list_filter = ('created_at',)
    search_fields = ('author__user__username', 'content')


    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = "Conteúdo"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'parent', 'created_at', 'total_likes')
    list_filter = ('created_at',)
    search_fields = ('author__user__username', 'content')