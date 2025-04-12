from django.utils.translation import gettext_lazy as _


class AuthMessages:
    POST_URL_ONLY = _("This URL is Post Request To Register ")
    DATABASE_ERROR = _("Database or Temporary authentication system issue")

    # Register
    REGISTER_SUCCESS = _(
        "User Registered successfully. Verification Code sent to (Mobile ~ E-Mail)."
    )
    REGISTER_FAILED = _("Registration Failed ")

    REGISTER_VALIDATION_ERROR = _("Invalid registration Data")
    REGISTER_DUPLICATE = _("User Already Exists")

    REGISTER_SUCCESS_BUT_EMAIL_FAILED = _(
        "Registration complete but verification email failed. Please contact support."
    )

    # Log In
    LOGIN_SUCCESS = _("Sign In Successfully.")
    LOGIN_ERROR = _("Failed Sign In.Error is >> ")
    USER_NOT_FOUND = _("Account Not Found.")
    PASSWORD_WRONG = _("Incorrect Password")
    VERIFY_ACCOUNT = _("Please Verfy Your Account before logging in.")

    INVALID_TOKEN = "Invalid authentication token"
    ACCOUNT_INACTIVE = "Your account is inactive"

    # Log Out
    LOGOUT_SUCCESS = _("Sign Out Successfully.")
    LOGOUT_ERROR = _("Error occurred during logout")

    # Forgot / Reset Password
    PASSWORD_RESET_EMAIL_SENT = _("Password Reset E-Mail sent if account exists")
    PASSWORD_RESET_ERROR = _("Failed Reset Password .Error is >> ")
    PASSWORDS_DO_NOT_MATCH = _("Passwords do not match")
    INVALID_RESET_LINK = _("Invalid Password Reset link")
    TOKEN_INVALID_OR_EXPIRED = _("Token Invalid or Expired")
    RESET_PASSWORD_SUCCESS = _("Password Reset Successfully.")
    RESET_PASSWORD_FAILED = _("Password Reset failed")

    PASSWORD_TOO_SHORT = _("Password must be at least 8 characters")
    PASSWORD_NO_NUMBER = _("Password must contain at least one number")
    PASSWORD_NO_UPPER = _("Password must contain at least one uppercase letter")

    INVALID_CREDENTIALS = _("Invalid Credentials Error")
    # E-Mail Verfication
    EMAIL_VERIFICATION_SUCCESS = _("Email verified successfully")
    INVALID_OTP = _("Invalid verification code")
    EMAIL_VERIFICATION_ERROR = _("Error verifying email")
    VALIDATION_ERROR = _("Validation error")
    OTP_EXPIRED = _("Verification code has expired")  # If you implement expiration

    EMAIL_ALREADY_VERIFIED = _("Email is already verified")

    # Mobile Verification
    MOBILE_VERIFICATION_SUCCESS = _("Mobile verified successfully")
    INVALID_MOBILE_FORMAT = _("Mobile must include country code (+XX...)")
    INVALID_FIREBASE_TOKEN = _("Invalid verification token")
    MOBILE_VERIFICATION_FAILED = _("Mobile verification failed")

    MOBILE_NUMBER_CONFLICT = _(
        "This mobile number is already associated with another account"
    )

    ############################ Firebase #############################
    TRY_AGAIN = _("Try Again")
    CORRECT = _("Correct")
    SUBSCRIPTION = _("Topic Subscription")
    PERMISSION_DENIED = _("Permission Denied")
    ############################ Firebase #############################

    # Firebase Admin Messages
    FIREBASE_USER = _("Firebase User")
    FIREBASE_ADMIN = _("Firebase Admin")

    FIREBASE_AUTH_ERROR = _("Firebase authentication error")
    FIREBASE_IMAGE_URL = _("Firebase Image URL")
    CLAIMS = _("Claims")
    FIREBASE_INTEGRATION_ERROR = _(
        "System temporarily unavailable. Please try again later."
    )
    FIREBASE_LOGOUT_ERROR = _("Error revoking Firebase session")
    RESOURCE_EXISTS = _("Resource already exists")
    RESOURCE_NOT_FOUND = _("Resource not found")
    INVALID_ARGUMENT = _("Invalid argument provided")
    FIREBASE_ERROR = _("Firebase operation Error: ")
    UNEXPECTED_ERROR = _("An unexpected error occurred: ")
    CONFIG_MISSING = _("Firebase configuration missing")
    FIREBASE_INIT_FAILED = _("Firebase initialization failed")
    EMAIL_ALREADY_EXISTS = _("Email already in use")
    PHONE_ALREADY_EXISTS = _("Phone number already in use")
    INVALID_TOKEN_AUDIENCE = _("Invalid token audience")
    # Pyrebase Messages
    PYREBASE = _("Pyrebase")
    PYREBASE_HTTP_ERROR = _("Firebase communication error")
    PYREBASE_ERROR = _("Firebase operation failed")
    PYREBASE_INIT_FAILED = _("Firebase initialization failed")
    CONFIG_MISSING = _("Firebase configuration missing")
    INVALID_EMAIL = _("Invalid email address")
    INVALID_PASSWORD = _("Invalid password")
    ############################ CustomAPIException #############################
    AUTHENTICATION_FAILED = _("Authentication failed")
    NOT_FOUND = _("Not Found")
    UNKNOWN_ERROR = _("Unknown error")
    SUCCESS = _("Success")
    REQUIRED = _("it is Required,must be Set.")
    FIREBASE_DELETE_ERROR = _("Unknown error")
