from django.urls import path

from searchapp import views as searchapp


app_name = 'searchapp'

urlpatterns = [
    path('', searchapp.search, name='search'),
]
