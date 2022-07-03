from django.urls import path

from commentapp import views as commentapp


app_name = 'commentapp'

urlpatterns = [
    path('delete/<int:pk>/', commentapp.comment_delete, name='delete'),
    path('add/<int:pk>/', commentapp.add_comment, name='add'),
]
