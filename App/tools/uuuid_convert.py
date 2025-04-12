import uuid
import base64


def uuid_to_urlsafe_base64(uuid_obj):
    """
    Convert a UUID to URL-safe Base64 (22 characters)

    Args:
        uuid_obj: UUID object or string

    Returns:
        str: URL-safe Base64 encoded string (without padding)
    """
    if isinstance(uuid_obj, str):
        uuid_obj = uuid.UUID(uuid_obj)

    # Convert UUID to 16-byte bytes
    uuid_bytes = uuid_obj.bytes

    # Encode to Base64 and make URL-safe
    base64_str = base64.urlsafe_b64encode(uuid_bytes).rstrip(b"=").decode("ascii")

    return base64_str


def urlsafe_base64_to_uuid(base64_str):
    """
    Convert URL-safe Base64 back to UUID

    Args:
        base64_str: 22-character URL-safe Base64 string

    Returns:
        UUID: Original UUID object
    """
    # Add padding if needed (Base64 needs length divisible by 4)
    padding = len(base64_str) % 4
    if padding:
        base64_str += "=" * (4 - padding)

    # Decode back to bytes
    uuid_bytes = base64.urlsafe_b64decode(base64_str)

    return uuid.UUID(bytes=uuid_bytes)
