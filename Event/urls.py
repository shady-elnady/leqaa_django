from django.urls import path

from .views import event_list, email

# Create your views here.

app_name = "Event"

urlpatterns = [
    path("all/", event_list, name="event_list"),
    path("email/", email, name="email"),
]
