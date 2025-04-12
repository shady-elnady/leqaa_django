from django.db.models.signals import post_save
from django.dispatch import receiver
from firebase_admin import messaging
from typing import Any

from Category.models import Category
from Event.models import Event
from User.models import User


@receiver(post_save, sender=Event)
def send_event_notifications(sender, instance, created, **kwargs):
    if created:  # Only send notifications for new events
        event: Event = instance
        category: Category = event.category

        users_to_notify: list[User] = get_users_to_notify(category)
        if users_to_notify.exists():
            message = create_notification_message(event, category, users_to_notify)
            send_notifications(message, category, event)


def get_users_to_notify(category: "Category") -> list["User"]:
    """Retrieve users who want notifications for a specific category."""
    return User.objects.filter(
        interesting_notifiable_categories=category,
        fcm_token__isnull=False,
    )


def create_notification_message(
    event: "Event", category: "Category", users_to_notify: list["User"]
):
    """Create a Firebase notification message."""
    return messaging.MulticastMessage(
        notification=messaging.Notification(
            title="New Event Alert!",
            body=f'A new event "{event.title}" in the category "{category.name}" has been added.',
            image=event.image,
        ),
        tokens=[user.fcm_token for user in users_to_notify],
    )


def send_notifications(message: Any, category: "Category", event: "Event"):
    """Send notifications and handle responses."""
    try:
        response = messaging.send_multicast(message)
        print(
            f'Successfully sent {response.success_count} notifications to users interested in category "{category.name}" for event "{event.title}".'
        )
        if response.failure_count > 0:
            print(f"Failed to send {response.failure_count} notifications.")
            log_failed_notifications(response, message)
    except Exception as e:
        print(f"Error sending Firebase notifications: {e}")


def log_failed_notifications(response, message):
    """Log details of failed notifications."""
    for i, resp in enumerate(response.responses):
        if not resp.success:
            print(f"Error sending to token {message.tokens[i]}: {resp.error}")
