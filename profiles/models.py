from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 
from django.dispatch import receiver




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    bio = models.TextField(max_length=300, blank=True, verbose_name="Biografia")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null="True", verbose_name="Foto de Perfil")

    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Se o usuário acabou de ser criado, cria um Profile para ele
        Profile.objects.create(user=instance)
    else:
        # Se o usuário apenas foi atualizado, garante que o Profile seja salvo
        instance.profile.save()


