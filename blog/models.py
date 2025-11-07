from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    LANG_CHOICES = (
        ("ar", "العربية"),
        ("en", "English"),
    )
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    language = models.CharField(max_length=2, choices=LANG_CHOICES, default="ar")
    excerpt = models.TextField(blank=True)
    body = models.TextField()
    cover = models.ImageField(upload_to="blog/covers/", blank=True, null=True)
    tags = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    publish_at = models.DateTimeField(default=timezone.now)

    # SEO
    meta_title = models.CharField(max_length=255, blank=True)
    meta_description = models.CharField(max_length=300, blank=True)
    og_image = models.ImageField(upload_to="blog/og/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publish_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            candidate = base
            counter = 1
            while BlogPost.objects.filter(slug=candidate).exclude(pk=self.pk).exists():
                counter += 1
                candidate = f"{base}-{counter}"
            self.slug = candidate
        super().save(*args, **kwargs)

    def is_published(self):
        return self.status == "published" and self.publish_at <= timezone.now()

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]


# Create your models here.
