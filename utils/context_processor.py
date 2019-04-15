from amazon import settings
from catalog.models import Category

def amazon(request):
    return {
        'request':request,
        'meta_keywords':settings.META_KEYWORDS
        'meta_description':settings.META_DESCRIPTION
        'site_name':settings.SITE_NAME
        'active_categories':Category.objects.filter(is_active = True)
    }