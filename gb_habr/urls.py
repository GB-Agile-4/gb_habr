from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from mainapp import views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('mainapp.urls', namespace='mainapp')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('user/', include('accountapp.urls', namespace='user')),
    path('articleapp/', include(('articleapp.urls', 'articleapp'), namespace='articleapp')),
    path('search/', include('searchapp.urls', namespace='search')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
