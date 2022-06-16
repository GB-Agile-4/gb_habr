from django.urls import path

from accountapp import views as userapp


app_name = 'accountapp'

urlpatterns = [
    path('', userapp.personal_area, name=''),
    path('create/', userapp.create_pub, name='create')
]
