from django.urls import path

from commentapp import views as commentapp


app_name = 'commentapp'

urlpatterns = [
    path('delete/<int:pk>/', commentapp.comment_delete, name='delete'),
]
