from django.apps import AppConfig


class ModerappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moderapp'

    def ready(self):
        from .views import start_scheduler
        start_scheduler()
