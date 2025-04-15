from django.shortcuts import render  # noqa: F401

from .models import Event

# Create your views here.
APP_NAME = "Event"


def event_list(request):
    """
    View to display a list of all events.
    """
    events = Event.objects.all()[:2]  # Retrieve all Event objects from the database
    return render(request, f"{APP_NAME}/event_list.html", {"events": events})


def email(request):
    """
    View to display a list of all events.

    """
    events = Event.objects.all()[:2]  # Retrieve all Event objects from the database
    context = {
        "otp": "555",
        "our_facebook_account_ulr": "https://www.facebook.com/",
        "our_twitter_account_ulr": "https://x.com/i/flow/login",
        "our_instagram_account_ulr ": "https://www.instagram.com/accounts/login/?hl=en",
        "our_linkedin_account_ulr  ": "https://www.linkedin.com/feed/",
        "events": events,
    }
    return render(request, r"emails/wasla_verfiy_email.html", context=context)
