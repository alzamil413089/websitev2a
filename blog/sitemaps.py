from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.utils import timezone
from .models import BlogPost


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return BlogPost.objects.filter(status="published", publish_at__lte=timezone.now())

    def lastmod(self, obj):
        return obj.updated_at or obj.publish_at

