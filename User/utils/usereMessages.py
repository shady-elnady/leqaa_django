from django.utils.translation import gettext_lazy as _


class UserMessages:
    # Phone Nmuber
    PHONE_INVALID_VALIDATION = _(
        "Invalid Phone Number,it must not consist of space and requires country code. eg : +2 01012345678."
    )
    MOBILE_UNIQUE_VALIDATION = _("Mobile must Unique")
    MOBILE_NOT_VERIFIED = _("Mobile is not Verified.")
    # E-Mail
    EMAIL_INVALID_VALIDATION = _("Invalid E-Mail")
    EMAIL_UNIQUE_VALIDATION = _("E-Mail must Unique")
    EMAIL_NOT_VERIFIED = _("E-mail is not Verified.")
    # Name
    NAME_INVALID_VALIDATION = _("Invalid Name , it must conatin 4 Names of Parents")
    NAME_UNIQUE_VALIDATION = _("Name must be Unique")
    # Password
    PASSWORD_INVALID_VALIDATION = _(
        "Invalid Password, it must contain one or more Upper Case Char, one or more Lower Case Char, one or more from [@, $ ,!, %, *, ?, &]; between 8 to 32 Chars"
    )
    # National ID
    NATIONAL_ID_INVALID_VALIDATION = _(
        "Invalid National ID, it must be 14 Numbers. eg : 11111111111111"
    )
    NATIONAL_ID_UNIQUE_VALIDATION = _("National ID must Unique")
    # User
    USER_NOT_VERIFIED = _("User Account is Not Verified.")
    USER_BLOCHED = _("User Account is Blocked.")
    USER_NOT_ACTIVATE = _("User Account is Not Activate.")
    USER_NOT_FOUND = _("User Account is Not Found.")
    # Key
    OTP_INVALID_VALIDATION = _("Invalid OTP Key, it must be 4 Numbers. eg : 4321")
