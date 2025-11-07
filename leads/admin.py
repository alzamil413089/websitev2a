from django.contrib import admin
from .models import Lead, Newsletter


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "utm_source", "created_at")
    list_filter = ("utm_source", "created_at")
    search_fields = ("name", "email", "phone", "message")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)


# Register your models here.
