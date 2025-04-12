from django.urls import path

from Notification.api.restAPI.views.fcm_token import update_fcm_token


app_name = "Notification"


urlpatterns = [
    path("fcm-token/", update_fcm_token, name="fcmToken"),
]
