from Event.models import Event
from Config.celery import shared_task
from django.conf import settings
from firebase_admin import messaging
from .models import User  # Import your User model


@shared_task
def send_firebase_notification(tokens, title, body, data=None):
    """
    Sends a Firebase notification to the specified tokens.
    """
    if not settings.FIREBASE_ADMIN_SDK_INITIALIZED:
        print("Firebase Admin SDK not initialized. Cannot send notification.")
        return

    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        data=data if data else {},
        tokens=tokens,
    )

    try:
        response = messaging.send_multicast(message)
        print(f"Successfully sent {response.success_count} notifications.")
        if response.failure_count > 0:
            for i, resp in enumerate(response.responses):
                if not resp.success:
                    print(
                        f"Error sending notification to token {tokens[i]}: {resp.exception}"
                    )
    except Exception as e:
        print(f"Error sending Firebase notification via Celery: {e}")


@shared_task
def notify_users_about_new_event_task(event_id):
    """
    Celery task to notify users about a new event.
    """
    # # Other Method
    # from django.apps import apps
    # Event = apps.get_model("your_app_name", "Event")  # Replace 'your_app_name'
    event: Event = Event.objects.get(pk=event_id)
    category = event.Category

    users_to_notify = User.objects.filter(
        Interests__category=category, fcm_token__isnull=False
    ).distinct()

    if not users_to_notify:
        print(
            f"No users found with favorite category: {category.name} for event {event.name}"
        )
        return

    tokens = [user.fcm_token for user in users_to_notify]
    title = "New Event Alert!"
    body = f'A new event "{event.name}" in your favorite category "{category.name}" has been added.'
    data = {
        "event_id": str(event.id),
        "event_name": event.name,
        "category_name": category.name,
        # Add other relevant data
    }

    send_firebase_notification.delay(tokens, title, body, data)
