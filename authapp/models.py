from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class HabrUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, verbose_name='Аватар')
    age = models.PositiveSmallIntegerField(verbose_name='Возраст', default=18)
    avatar_url = models.CharField(max_length=128, blank=True, null=True)
    # activate_key = models.CharField(max_length=128, verbose_name='Ключ активации', blank=True, null=True)
    # activate_key_expired = models.DateTimeField(blank=True, null=True)
    #
    # def is_activate_key_expired(self):
    #     if datetime.now(pytz.timezone(settings.TIME_ZONE)) > self.activate_key_expired + timedelta(hours=48):
    #         return True
    #     return False
    #
    # def activate_user(self):
    #     self.is_active = True
    #     self.activate_key = None
    #     self.activate_key_expired = None
    #     self.save()


class HabrUserProfile(models.Model):
    user = models.OneToOneField(HabrUser, null=False, unique=True, on_delete=models.CASCADE, db_index=True)
    tagline = models.CharField(max_length=128, verbose_name='Тэги', blank=True)
    about_me = models.TextField(verbose_name='Обо мне')

    @receiver(post_save, sender=HabrUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            HabrUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=HabrUser)
    def update_user_profile(sender, instance, **kwargs):
        instance.habruserprofile.save()


from django.db import models

# Create your models here.
