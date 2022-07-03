from django.urls import path
from . import views

app_name = 'like'

urlpatterns = [
    path('add_like/<int:pk>/', views.add_like, name='add_like'),
    path('add_dislike/<int:pk>/', views.add_dislike, name='add_dislike'),
    path('comment_like/<int:pk>/', views.comment_like, name='comment_dlike'),
    path('comment_dislike/<int:pk>/', views.comment_dislike, name='comment_dislike'),
]
