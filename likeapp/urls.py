from django.urls import path
from . import views

app_name = 'like'

urlpatterns = [
    path('add_like/<int:pk>/', views.add_like, name='add_like'),
    path('add_dislike/<int:pk>/', views.add_dislike, name='add_dislike'),
]
