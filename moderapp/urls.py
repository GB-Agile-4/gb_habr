from django.urls import path
from moderapp import views as moderapp


app_name = 'moderapp'

urlpatterns = [
    path('ban_user/<int:pk>/', moderapp.ban_user, name='ban_user'),

    path('moderate_list/', moderapp.moderate_list, name='moderate_list'),
    path('moderate_post/<int:pk>/', moderapp.moderate_post, name='moderate_post'),
    path('confirm_moderate_post/<int:pk>/', moderapp.confirm_moderate_post, name='confirm_moderate_post'),
    path('reject_moderate_post/<int:pk>/', moderapp.reject_moderate_post, name='reject_moderate_post'),

]
