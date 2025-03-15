from django.core.mail import EmailMessage
import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class EMailUtil:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        EmailThread(email).start()


"""

EmailMessage(
    subject: str = ...,
    body: str | None = ...,
    from_email: str | None = ...,
    to: Sequence[str] | None = ...,
    bcc: Sequence[str] | None = ...,
    connection: Any | None = ...,
    attachments: Sequence[_AttachmentTuple | MIMEBase] | None = ...,
    headers: dict[str, str] | None = ...,
    cc: Sequence[str] | None = ...,
    reply_to: Sequence[str] | None = ...
)


notice_html = render_to_string("emails/verify-email.html", {"otp": message})

send_mail(
    subject="Verify Your E-Mail",
    message=message,
    recipient_list=[instance.email],
    from_email=settings.EMAIL_HOST_USER,
    fail_silently=False,
    html_message=notice_html,
)


send_mail(
    subject: str,
    message: str,
    from_email: str | None,
    recipient_list: list[str],
    fail_silently: bool = ...,
    auth_user: str | None = ...,
    auth_password: str | None = ...,
    connection: Any | None = ...,
    html_message: str | None = ...
)

"""
