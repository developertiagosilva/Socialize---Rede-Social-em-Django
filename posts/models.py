from django.db import models
from profiles.models import Profile


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=1000, verbose_name="Conteúdo do Post")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # --- CAMPO E HELPER ADICIONADOS ---
    likes = models.ManyToManyField(Profile, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post de {self.author.user.username} - {self.created_at.strftime('%d/%m/%y %H:%M')}"
    
    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500, verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    likes = models.ManyToManyField(Profile, related_name='liked_comments', blank=True)

    class Meta:
        ordering = ['created_at']  

    def __str__(self):
        return f"Comentário de {self.author.user.username} em {self.post.id}"
    
    @property
    def total_likes(self):
        return self.likes.count()