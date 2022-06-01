from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def register(request):
    pass


def login(request):
    pass


def edit(request):
    pass


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def verify(request):
    pass
