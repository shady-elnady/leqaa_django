import logging
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from typing import List, Optional, Dict, Any, Union

logger = logging.getLogger(__name__)


def send_my_email(
    recipient_list: List[str],
    subject: str,
    template_name: Union[List[str], str],
    context: Optional[Dict[str, Any]] = None,
    plain_message: Optional[str] = None,
    from_email: Optional[str] = None,
    fail_silently: bool = False,
) -> int:
    """
    Send email with HTML and plain text alternatives.

    Args:
        recipient_list: List of recipient email addresses
        subject: Email subject
        template_name: Template path or list of template paths for HTML content
        context: Context data for template rendering
        plain_message: Plain text version of the email (optional)
        from_email: Sender email address (defaults to settings.EMAIL_HOST_USER)
        fail_silently: If True, exceptions will be suppressed

    Returns:
        Number of successfully sent emails (0 or 1)

    Raises:
        Exception: If fail_silently is False and error occurs
    """
    try:
        # Prepare email parameters
        from_email = from_email or settings.EMAIL_HOST_USER
        context = context or {}

        # Render HTML content
        html_message = render_to_string(template_name, context)

        # If no plain text provided, use the HTML content stripped of tags
        if plain_message is None:
            from django.utils.html import strip_tags

            plain_message = strip_tags(html_message)

        logger.info(
            f"Attempting to send email to {recipient_list} with subject: {subject}",
            extra={
                "recipient_count": len(recipient_list),
                "subject": subject,
                "from_email": from_email,
            },
        )

        # Send email
        result = send_mail(
            subject=subject,
            message=plain_message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message,
            fail_silently=fail_silently,
        )

        logger.info(
            f"Successfully sent email to {recipient_list}",
            extra={
                "success_count": result,
                "subject": subject,
            },
        )

        return result

    except Exception as e:
        logger.error(
            f"Failed to send email to {recipient_list}: {str(e)}",
            exc_info=True,
            extra={
                "subject": subject,
                "recipients": recipient_list,
                "error": str(e),
            },
        )

        if not fail_silently:
            raise
        return 0
