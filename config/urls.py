"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.i18n import i18n_patterns
from core.sitemaps import StaticViewSitemap
from blog.sitemaps import BlogSitemap
from blog.feeds import LatestPostsFeed
from core.views import robots_txt, health

urlpatterns = [
    # Redirect root to default language (Arabic)
    path('', RedirectView.as_view(url='/ar/', permanent=False)),
    # language switcher endpoint (no language prefix)
    path('i18n/', include('django.conf.urls.i18n')),
    # Non-i18n endpoints
    path('sitemap.xml', sitemap, {
        'sitemaps': {
            'static': StaticViewSitemap,
            'blog': BlogSitemap,
        }
    }, name='sitemap'),
    path('rss.xml', LatestPostsFeed(), name='rss'),
    path('robots.txt', robots_txt, name='robots'),
    path('health/', health, name='health'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('leads/', include('leads.urls', namespace='leads')),
)
