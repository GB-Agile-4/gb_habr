from django.urls import path
from userapp import views as userapp


app_name = 'userapp'

urlpatterns = [
    path('', userapp.personal_area),
    path('create/', userapp.create_pub, name='create')
]