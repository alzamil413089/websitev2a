from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return ["core:home", "core:about", "core:services", "core:contact"]

    def location(self, item):
        return reverse(item)

