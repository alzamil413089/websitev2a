from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def contact(request):
    return render(request, "core/contact.html")


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: /sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def health(request):
    return HttpResponse("ok", content_type="text/plain")

