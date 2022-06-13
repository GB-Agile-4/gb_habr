from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from authapp.models import HabrUser, HabrUserProfile
from django import forms


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

    # def save(self, *args, **kwargs):
    #     user = super().save(*args, **kwargs)
    #     user.is_active = False
    #
    #     user.save()
    #     return user


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