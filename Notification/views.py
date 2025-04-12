from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from firebase_admin import messaging
import json
import requests


def ssend_notification(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            registration_token = data.get("token")
            message = messaging.Message(
                notification=messaging.Notification(
                    title="Notification Title",
                    body="Notification Body",
                ),
                token=registration_token,
            )
            response = messaging.send(message)
            return JsonResponse({"message": f"Notification sent: {response}"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


##########

FCM_SERVER_KEY = "your-server-key"


def send_notification(token, title, message):
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        "Authorization": f"key={FCM_SERVER_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "to": token,
        "notification": {"title": title, "body": message},
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()


def notify_user(request):
    token = request.GET.get("token")
    title = "Hello!"
    message = "This is a Firebase notification."

    response = send_notification(token, title, message)
    return JsonResponse(response)
