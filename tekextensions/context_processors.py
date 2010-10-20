from django.conf import settings

def admin_media_prefix(request):
    return {'ADMIN_MEDIA_PREFIX': settings.ADMIN_MEDIA_PREFIX }
