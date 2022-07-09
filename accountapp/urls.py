from django.urls import path

from accountapp import views as account


app_name = 'accountapp'

urlpatterns = [
    path('notifications/', account.notifications_list, name='notifications'),
    path('notifications/delete/<int:pk>', account.notifications_delete, name='notifications-delete'),
    path('<slug:slug>/', account.personal_area, name='account'),
]
