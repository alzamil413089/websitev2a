from django.conf import settings


def default_seo(request):
    return {
        "SITE_NAME": getattr(settings, "SITE_NAME", "Fyntralink"),
        "DEFAULT_META_TITLE": getattr(settings, "DEFAULT_META_TITLE", "Fyntralink"),
        "DEFAULT_META_DESC": getattr(settings, "DEFAULT_META_DESC", ""),
        "DEFAULT_META_IMAGE": getattr(settings, "DEFAULT_META_IMAGE", ""),
    }

