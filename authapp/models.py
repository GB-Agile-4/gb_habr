from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class HabrUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=18)
    avatar_url = models.CharField(max_length=128, blank=True, null=True)
    is_banned = models.BooleanField(default=False)


class HabrUserProfile(models.Model):
    user = models.OneToOneField(HabrUser, null=False, unique=True, on_delete=models.CASCADE, db_index=True)
    tagline = models.CharField(max_length=128, verbose_name='Тэги', blank=True)
    about_me = models.TextField(verbose_name='Обо мне')

    @receiver(post_save, sender=HabrUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            HabrUserProfile.objects.create(user=instance)
        instance.habruserprofile.save()
