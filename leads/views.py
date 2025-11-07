from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from .forms import LeadForm, NewsletterForm


def contact_submit(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            lead = form.save(commit=False)
            lead.utm_source = request.GET.get("utm_source", "")
            lead.save()
            # Redirect back to contact with ok flag
            return redirect(f"{reverse('core:contact')}?ok=1")
    # Fallback redirect
    return redirect(reverse("core:contact"))


def newsletter_subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception:
                # Ignore duplicates due to unique constraint
                pass
        # redirect to referrer or home
        next_url = request.META.get("HTTP_REFERER") or reverse("core:home")
        if not url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            next_url = reverse("core:home")
        return redirect(next_url)
    return redirect(reverse("core:home"))

