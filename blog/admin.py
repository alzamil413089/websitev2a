from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "language", "status", "publish_at")
    list_filter = ("language", "status", "publish_at")
    search_fields = ("title", "excerpt", "body", "tags")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish_at"


# Register your models here.
