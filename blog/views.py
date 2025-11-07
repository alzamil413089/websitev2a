from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import BlogPost


def _published_qs():
    return BlogPost.objects.filter(status="published", publish_at__lte=timezone.now())


def post_list(request):
    lang = request.LANGUAGE_CODE
    posts = _published_qs().filter(language=lang)
    return render(request, "blog/list.html", {"posts": posts})


def tag_filter(request, tag):
    lang = request.LANGUAGE_CODE
    posts = _published_qs().filter(language=lang, tags__icontains=tag)
    return render(request, "blog/list.html", {"posts": posts, "active_tag": tag})


def post_detail(request, slug):
    lang = request.LANGUAGE_CODE
    post = get_object_or_404(_published_qs().filter(language=lang), slug=slug)
    return render(request, "blog/detail.html", {"post": post})

