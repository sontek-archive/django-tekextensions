from django.conf import settings
from django.contrib.sites.models import Site, RequestSite

def admin_media_prefix(request):
    return {'ADMIN_MEDIA_PREFIX': settings.ADMIN_MEDIA_PREFIX }

def current_site(request):
    '''
    A context processor to add the "current_site" to the current Context
    '''
    context_name = 'CURRENT_SITE'

    try:
        current_site = Site.objects.get_current()
        return { context_name: current_site, }
    except Site.DoesNotExist:
        # always return a dict, no matter what!
        return { context_name: RequestSite(request)}
