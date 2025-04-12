from django.urls import path
from event_master.views import (
    index,
    about,
    spakers,
    schedule,
    blog,
    blog_details,
    contact,
    elements,
    splash,
)


app_name = "event_master"

urlpatterns = [
    path("", splash, name="Splash"),
    path("home/", index, name="Home"),
    path("about/", about, name="About"),
    path("spakers/", spakers, name="Spakers"),
    path("schedule/", schedule, name="Schedule"),
    path("blog/", blog, name="Blog"),
    path("blog_details/", blog_details, name="BlogDetails"),
    path("contact/", contact, name="Contact"),
    path("elements/", elements, name="Elements"),
]
