import hashlib
from random import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import HabrUser, HabrUserProfile
from django import forms

from datetime import datetime, timedelta

import pytz
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class HabrUserLoginForm(AuthenticationForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class HabrUserRegisterForm(UserCreationForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'first_name', 'last_name', 'avatar', 'email', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.is_active = False

        # salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        # user.activate_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()

        user.activate_key = hashlib.sha1(user.email.encode('utf8')).hexdigest()
        user.activate_key_expired = datetime.now(pytz.timezone(settings.TIME_ZONE))

        user.save()
        return  user


class HabrUserEditForm(UserChangeForm):
    class Meta:
        model = HabrUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()


class HabrUserProfileEditForm(forms.ModelForm):
    class Meta:
        model = HabrUserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''