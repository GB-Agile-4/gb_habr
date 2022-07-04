from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='default_avatar')
def default_avatar(path_img):
    if not path_img:
        path_img = "users_avatars/default.png"
    return f"{settings.MEDIA_URL}{path_img}"
