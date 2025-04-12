from django.db.models import Max
from os.path import join

from App.tools import get_model_name_from_instance


def upload_image_to(instance, filename):
    """
    Generates an upload path for images with the structure:
    images/<model_name>/<user_or_event_uid>/<instance_uid_or_id>.<ext>

    Args:
        instance: Model instance being saved
        filename: Original filename of the uploaded image

    Returns:
        str: Generated upload path
    """
    # Clean and normalize model name
    model_name = get_model_name_from_instance(instance)

    path_parts = [
        "images",
        model_name,
    ]

    # Add user/event identifier if available
    if hasattr(instance, "user") and hasattr(instance.user, "uid"):
        path_parts.append(str(instance.user.uid))
    elif hasattr(instance, "event") and hasattr(instance.event, "uid"):
        path_parts.append(str(instance.event.uid))

    # Determine filename
    if hasattr(instance, "uid"):
        file_id = instance.uid_to_urlsafe_base64
    else:
        max_id = instance.__class__.objects.aggregate(Max("id"))["id__max"] or 0
        file_id = str(max_id + 1)

    # Get file extension safely
    file_ext = filename.split(".")[-1].lower() if "." in filename else "jpg"
    valid_extensions = {"jpg", "jpeg", "png", "gif", "webp"}
    file_ext = file_ext if file_ext in valid_extensions else "jpg"

    return join(*path_parts, f"{file_id}.{file_ext}")
