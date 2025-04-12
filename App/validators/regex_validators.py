from django.core.validators import RegexValidator
import re

from App.messages import ValidationMessages


class RegexValidators:
    """
    Class to hold regexes for User models in userapp.
    """

    FULL_NAME_REGEX = re.compile(r"^[a-zA-Z0-9]+$")

    ## prithoo: Full ISO Spec 10 to 12 digit phone number (+(ISD)(STD)(AREA)(SUBSCRIBER)):
    ##  8811098879, 881-109-8879, +918811098879, +91-881-109-8879, +91-361-222-0324, +913612220324
    ## confirmed on 'https://regex101.com/'
    TELEPHONE_REGEX_ISD = re.compile(
        r"^(\+\d{0,2})?([\s.-])?(\+\d{1,2}\s)?\(?\d{3}\)?([\s.-])?\d{3}([\s.-])?\d{4}$"
    )
    # ## Normal 10-digit phone number ((STD)(AREA)(SUBSCRIBER))
    # PHONE_REGEX = re.compile(
    #     r"^([\s.-])?(\+\d{1,2}\s)?\(?\d{3}\)?([\s.-])?\d{3}([\s.-])?\d{4}$"
    # )

    MOBILE_REGEX = re.compile(
        r"^\+?(\d{1,3})[\s.-]?(\d{2,4})[\s.-]?(\d{3})[\s.-]?(\d{3,4})$"
    )

    ##
    NATIONAL_ID_REGEX = re.compile(
        r"^\d{14}$",
    )

    OTP_REGEX = re.compile(r"^\d{4}$")

    TELEPHONE_COUNTRY_CODE_REGEX = re.compile(r"^\+?1?\d{1,3}$")

    # >=1 UC char, >=1 LC char, >=1 NUM char >=[@, $ ,!, %, *, ?, &]; between 8 to 32 chars; confirmed on 'https://regex101.com/'
    PASSWORD_REGEX = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$"
    )

    full_name_pattern_validator = RegexValidator(
        regex=[FULL_NAME_REGEX],
        message=ValidationMessages.FULL_NAME_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    telephone_country_code_pattern_validator = RegexValidator(
        regex=TELEPHONE_COUNTRY_CODE_REGEX,
        message=ValidationMessages.TELPHONE_COUNTRY_CODE_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    governorate_tel_code_pattern_validator = RegexValidator(
        regex=r"^\d{1,3}$",
        message=ValidationMessages.GOVERNORATE_TELPHONE_CODE_INVALID_PATTERN_VALIDATION_MESSAGE,
    )

    telephone_pattern_validator = RegexValidator(
        regex=TELEPHONE_REGEX_ISD,
        message=ValidationMessages.TELPHONE_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    mobile_pattern_validator = RegexValidator(
        regex=MOBILE_REGEX,
        message=ValidationMessages.MOBILE_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    otp_pattern_validator = RegexValidator(
        regex=OTP_REGEX,
        message=ValidationMessages.OTP_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    full_name_pattern_validator = RegexValidator(
        regex=FULL_NAME_REGEX,
        message=ValidationMessages.FULL_NAME_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    password_pattern_validator = RegexValidator(
        regex=PASSWORD_REGEX,
        message=ValidationMessages.PASSWORD_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    national_id_pattern_validator = RegexValidator(
        regex=NATIONAL_ID_REGEX,
        message=ValidationMessages.NATIONAL_ID_INVALID_PATTERN_VALIDATION_MESSAGE,
        code="400",
    )

    # # Old code
    # @staticmethod
    # def get_mobile_pattern_validator(cls) -> "RegexValidator":
    #     return RegexValidator(
    #         regex=RegexValidators.MOBILE_REGEX,
    #         message=ValidationMessages.PHONE_INVALID_PATTERN_VALIDATION_MESSAGE,
    #         code="400",
    #     )

    @staticmethod
    def check_is_mobile(cls, unknown: str) -> bool:
        # for Mobile Number
        if RegexValidators.MOBILE_REGEX.fullmatch(unknown):
            return True
        else:
            return False

    @staticmethod
    def check_is_national_id(cls, unknown: str) -> bool:
        # for National ID
        if RegexValidators.NATIONAL_ID_REGEX.fullmatch(unknown):
            return True
        else:
            return False
