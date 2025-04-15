from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

from User.models import User, Profile, Lecturer, Student
from User.utils.enums import USERS_TYPES
from App.helpers import send_my_email


## Signal to Create Profile for each new User
@receiver(post_save, sender=User)
def create_user_profile_signal(sender, instance: "User", created: bool, **kwargs):
    if created:
        Token.objects.create(user=instance)

        if instance.user_type == USERS_TYPES.Student:
            Student.objects.create(user=instance)
        elif instance.user_type == USERS_TYPES.Lecturer:
            Lecturer.objects.create(user=instance)

        # Save Profile if Not Exist
        Profile.objects.create(user=instance)
        instance.Profile.save()

        if instance.email and not instance.email_verified_at:
            from Event.models import Event

            send_my_email(
                subject="Verify Your E-Mail",
                plain_message=instance.otp,
                recipient_list=[instance.email],
                template_name="emails/wasla_verfiy_email.html",
                context={
                    "events": Event.objects.all()[:2],
                    "otp": instance.otp,
                    "verification_url": instance.get_email_verification_url(),
                    "our_facebook_account_ulr": "https://www.facebook.com/",
                    "our_twitter_account_ulr": "https://x.com/i/flow/login",
                    "our_instagram_account_ulr ": "https://www.instagram.com/accounts/login/?hl=en",
                    "our_linkedin_account_ulr  ": "https://www.linkedin.com/feed/",
                },
            )
