try:
    import debug_toolbar.urls as dt_urls
except ImportError:
    dt_urls = None

if dt_urls:

    from django.conf import settings
    from django.conf.urls import patterns, include

    from .urls import urlpatterns

    debug_toolbar.urls.urlpatterns += patterns('',
        ('', include(urlpatterns)),
    )
