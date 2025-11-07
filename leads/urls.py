from django.urls import path
from . import views

app_name = "leads"

urlpatterns = [
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("newsletter/subscribe/", views.newsletter_subscribe, name="newsletter_subscribe"),
]

