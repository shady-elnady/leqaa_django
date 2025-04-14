from django.utils.translation import gettext_lazy as _


class ValidationMessages:
    # Country Telephone Code
    TELPHONE_COUNTRY_CODE_INVALID_PATTERN_VALIDATION_MESSAGE = _("❌")
    TELPHONE_COUNTRY_CODE_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌")
    # Governorate Telephone Code
    GOVERNORATE_TELPHONE_CODE_INVALID_PATTERN_VALIDATION_MESSAGE = _(
        "Governorate Telephone Code must be from 1 t 3 digits allowed. ❌"
    )
    GOVERNORATE_TELPHONE_CODE_INVALID_UNIQUE_VALIDATION_MESSAGE = _(
        "Governorate Telephone Code must be from 1 t 3 digits allowed. ❌"
    )
    # Mobile
    MOBILE_INVALID_PATTERN_VALIDATION_MESSAGE = _(
        "❌ Enter valid Mobile.Like (+20 10 123 4567|+20101234567|+20-10-123-4567)"
    )
    MOBILE_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌ Mobile is Used. choose Another")
    MOBILE_REQUIRED_VALIDATION_MESSAGE = _("❌ Mobile Number is Required")
    # Telephone
    TELPHONE_INVALID_PATTERN_VALIDATION_MESSAGE = _(
        "❌ Enter valid Phone.Like +91 98765 43210  | +1 415 555 1234 | +44 20 7946 0958 | +49 176 1234 5678 | +81 90 1234 5678 | +61 412 345 678 | +33 6 12 34 56 78 | 971501234567 | 65-6123-4567 | 852.5123.4567"
    )
    TELPHONE_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌")
    # OTP
    OTP_INVALID_PATTERN_VALIDATION_MESSAGE = _("❌")
    # National ID
    NATIONAL_ID_INVALID_PATTERN_VALIDATION_MESSAGE = _("❌")
    NATIONAL_ID_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌")
    # Password
    PASSWORD_INVALID_PATTERN_VALIDATION_MESSAGE = _("❌")
    # Full Name
    FULL_NAME_INVALID_PATTERN_VALIDATION_MESSAGE = _("❌")
    FULL_NAME_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌")
    # User Name
    USER_NAME_INVALID_UNIQUE_VALIDATION_MESSAGE = _(
        "❌ User Name is Used. Choose Another"
    )
    # E-Mail
    EMAIL_INVALID_UNIQUE_VALIDATION_MESSAGE = _("❌ E-Mail is Used. Choose Another")
    # Password
    PASSWORD_INVALID_PATTERN_VALIDATION_MESSAGE = _(
        "❌ Invalid Password, it must contain one or more Upper Case Char, one or more Lower Case Char, one or more from [@, $ ,!, %, *, ?, &]; between 8 to 32 Chars"
    )

    END_DATE_TIME_MUST_BE_AFTER_START_DATE_TIME = (
        "End datetime must be after start datetime"
    )

    """
    Semantic validation messages with visual symbols
    Symbols: ❌ (Error), ⚠️ (Warning), ℹ️ (Info), ✅ (Success)
    """

    # ==================== Phone Validation ====================
    MOBILE_INVALID = _(
        "❌ Invalid mobile format. "
        "ℹ️ Examples: \n"
        "• +201012345678 (Egypt)\n"
        "• +966501234567 (Saudi)\n"
        "• +971501234567 (UAE)\n"
        "⚠️ Include country code, no spaces or special chars"
    )

    MOBILE_EXISTS = _(
        "❌ Mobile already registered\n ⚠️ Use password recovery or try another number"
    )

    MOBILE_REQUIRED = _("❌ Mobile number required\n ℹ️ Needed for account verification")

    # ==================== OTP/Verification ====================
    OTP_INVALID = _(
        "❌ Invalid verification code\n ⚠️ Check SMS and enter {} -digit code"
    )

    OTP_MAX_LENGTH = _(
        "❌ Invalid code length\n ℹ️ Enter a {}-digit code sent to your E-Mail"
    )

    OTP_MIN_LENGTH = _(
        "❌ Invalid code length\n ℹ️ Enter a {}-digit code sent to your E-Mail"
    )

    OTP_EXPIRED = _("❌ Code expired\n ℹ️ Request new code (valid for 10 mins)")

    # ==================== Personal Information ====================
    NATIONAL_ID_INVALID = _(
        "❌ Invalid national ID\n"
        "⚠️ Must be 14 digits (Egypt) or your country's standard format"
    )

    NATIONAL_ID_EXISTS = _(
        "❌ ID already registered\n ⚠️ Contact support if this is your ID"
    )

    # ==================== Authentication ====================
    PASSWORD_WEAK = _(
        "❌ Weak password\n"
        "✅ Requirements:\n"
        "- 8-32 characters\n"
        "- Upper + lowercase\n"
        "- Number (123)\n"
        "- Symbol (@$!%*?&)"
    )

    # ==================== Account Information ====================
    USERNAME_TAKEN = _("❌ Username unavailable\n ℹ️ Try adding numbers (ahmed123)")

    EMAIL_EXISTS = _(
        "❌ Email already registered\n ⚠️ Use password recovery if this is yours"
    )

    EMAIL_INVALID = _("❌ Invalid email format\n ℹ️ Example: user@example.com")

    # ==================== System Codes ====================
    COUNTRY_CODE_INVALID = _(
        "❌ Invalid country code\n ℹ️ Must be 1-3 digits (20 for Egypt)"
    )

    REGION_CODE_INVALID = _(
        "❌ Invalid region code\n ℹ️ Example: 02 for Cairo, 03 for Alexandria"
    )

    # ==================== Form Structure ====================
    REQUIRED_FIELD = _(
        "❌ Required field missing\n ⚠️ Please complete all marked fields"
    )

    USER_TYPE_INVALID_VALIDATION_MESSAGE = _(
        "❌ Invalid User Type \n ℹ️ Choose from available options"
    )
    INVALID_CHOICE = _("❌ Invalid selection\n ℹ️ Choose from available options")

    # ==================== Success Messages ====================
    VALIDATION_OK = _("✅ All inputs valid\n ℹ️ You may proceed")

    PERMISSION_ERROR = _(
        "❌ Permission denied\n ⚠️ You don't have access to this resource"
    )
