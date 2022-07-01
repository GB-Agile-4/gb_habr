from django.urls import path

from accountapp import views as account


app_name = 'accountapp'

urlpatterns = [
    path('<slug:slug>/', account.personal_area, name='account'),
]
