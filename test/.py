import random
import string


def generate_otp(length=4):
    characters = string.digits
    otp = "".join(random.choice(characters) for _ in range(length))
    return otp


print(generate_otp())
