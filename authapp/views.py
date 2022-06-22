from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth

from authapp.forms import HabrUserLoginForm, HabrUserRegisterForm, HabrUserEditForm, HabrUserProfileEditForm
from authapp.models import HabrUser


def login(request):
    login_form = HabrUserLoginForm(data=request.POST)

    next_param = request.GET.get('next', '')

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)

            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])

            return HttpResponseRedirect(reverse('mainapp:index'))

    context = {
        'login_form': login_form,
        'next': next_param
    }

    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('mainapp:index'))


def register(request):
    if request.method == 'POST':
        register_form = HabrUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        register_form = HabrUserRegisterForm()

    context = {
        'register_form': register_form
    }

    return render(request, 'authapp/register.html', context)


def edit(request):
    if request.method == 'POST':
        edit_form = HabrUserEditForm(request.POST, request.FILES, instance=request.user)
        edit_profile_form = HabrUserProfileEditForm(request.POST, instance=request.user.habruserprofile)

        if edit_form.is_valid() and edit_profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = HabrUserEditForm(instance=request.user)
        edit_profile_form = HabrUserProfileEditForm(instance=request.user.habruserprofile)

    context = {
        'edit_form': edit_form,
        'edit_profile_form': edit_profile_form
    }

    return render(request, 'authapp/edit.html', context)


def verify(request, email, key):
    user = HabrUser.objects.filter(email=email).first()
    user.backend = 'django.contrib.auth.backends.ModelBackend'

    if user:
        if user.activate_key == key and not user.is_activate_key_expired():
            user.activate_user()
            auth.login(request, user)

    return render(request, 'authapp/register_result.html')
