from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

from User.models import User, Profile, Lecturer, Student
from User.utils.enums import USERS_TYPES


## Signal to Create Profile for each new User
@receiver(post_save, sender=User)
def create_signal(sender, instance: User, created: bool, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Token.objects.create(user=instance)

        if instance.user_type == USERS_TYPES.Student:
            Student.objects.create(user=instance)
        elif instance.user_type == USERS_TYPES.Lecturer:
            Lecturer.objects.create(user=instance)

        if not instance.email_verified_at:

            message = instance.otp
            # Add the message to render_to_string to use it in template
            notice_html = render_to_string("emails/verify-email.html", {"otp": message})

            send_mail(
                subject="Verify Your E-Mail",
                message=message,
                recipient_list=[instance.email],
                from_email=settings.EMAIL_HOST_USER,
                fail_silently=False,
                html_message=notice_html,
            )
    instance.Profile.save()


# leqaa
# uliy cfbt wmqq zdrm


"""

    from django.core.mail import EmailMultiAlternatives, get_connection

    # By default fail_silently is already False
    connection = get_connection(fail_silently=False)

    message = "A curated message based on the design the customer purchased."
    notice_html = render_to_string('MY_app/email-template.html', { "message": message })
    subject = 'Your New Design Confirmation'

    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=from_email
        to=recipient_list,
        connection=connection
    )
    email.attach_alternative(notice_html, "text/html")
    email.send()

"""
