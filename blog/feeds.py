from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils import timezone
from .models import BlogPost


class LatestPostsFeed(Feed):
    title = "Fyntralink Blog"
    link = "/blog/"
    description = "Latest posts from Fyntralink"

    def items(self):
        return (
            BlogPost.objects.filter(status="published", publish_at__lte=timezone.now())
            .order_by("-publish_at")[:20]
        )

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt or item.body[:300]

    def item_link(self, item):
        return reverse("blog:detail", kwargs={"slug": item.slug})

