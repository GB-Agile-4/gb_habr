"""gb_habr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mainapp import views as mainapp
from article import views as article


urlpatterns = [
    path('', mainapp.index, name='index'),

    path('admin/', admin.site.urls),

    path('content/', include('mainapp.urls', namespace='content')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('user/', include('accountapp.urls', namespace='user')),
    path('article/', include(('article.urls', 'article'), namespace='article')),
    path('search/', include('searchapp.urls', namespace='search')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
