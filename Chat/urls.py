from django.urls import path

from .views import chat_view, other_chat_view, whatss_chat_view


app_name = "Chat"


urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("other-chat/", other_chat_view, name="otherChat"),
    path("whatss-chat/", whatss_chat_view, name="whatssChat"),
]
