import base64
from datetime import datetime
from email.message import EmailMessage
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status, generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from requests.exceptions import HTTPError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

from django.contrib.auth import update_session_auth_hash

from API.utils.TwilioMessageHandler import TwilioMessageHandler
from User.utils.check_email import check_is_email
from API.api.Serializers.LogIn import LogInSerializer
from API.api.Serializers.Password import ChangePasswordSerializer
from django.contrib.auth import update_session_auth_hash
from API.utils.otp import generate_otp, send_otp_email

# # Create your views here.

User = get_user_model()


class UserLoginView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LogInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        national_id = str(request.data["national_id"])
        password = str(request.data["password"])
        try:
            user = User.objects.filter(national_id=national_id).first()
            if user is None or not user.check_password(password):
                return Response(
                    {
                        "success": False,
                        "message": "User Not Found",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                # login(request, user=user)
                token, _ = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "success": True,
                        "message": "User logged successfully",
                        "token": token.key,
                        "data": {
                            "user_id": user.id,
                            "username": user.username,
                            "email": user.email,
                            "is_verified": user.is_verified,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": f"Error is {e}, with type {type(e)}",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


"""
        curl -X POST \
        http://127.0.0.1/api/register-by-access-token/social/google-oauth2/ \
        -H 'Accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{"access_token": "<GoogleOAuth2-ACCESS-TOKEN-FROM-CLIENT>"}'

"""


@permission_classes([AllowAny])
class MobileSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            mobile_number = str(request.data.get("mobile"))
            user_id = str(request.data.get("user_id"))
            methodOtp = str(request.data.get("methodOtp"))
            if mobile_number and user_id:
                mobile = str(mobile_number)
                user = User.objects.get(id__iexact=user_id)
                # otp_key = generate_otp()
                otp_key = "ABCD"
                if user is not None:
                    messagehandler = None
                    if methodOtp == "methodOtpWhatsapp":
                        messagehandler = TwilioMessageHandler(
                            mobile, otp_key
                        ).send_otp_via_whatsapp()
                    else:
                        messagehandler = TwilioMessageHandler(
                            mobile, otp_key
                        ).send_otp_via_message()
                    if messagehandler is None:
                        return Response(
                            {
                                "success": False,
                                "message": "Error Connection To Server",
                                "status": status.HTTP_404_NOT_FOUND,
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    else:
                        user.otp = otp_key
                        user.mobile = mobile
                        user.save()
                        return Response(
                            {
                                "success": True,
                                "message": "Succes send OTP Go To Your Mobile",
                                "status": status.HTTP_202_ACCEPTED,
                                "data": {
                                    "user_id": user.id,
                                    "is_verified": user.is_verified,
                                },
                            },
                            status=status.HTTP_202_ACCEPTED,
                        )
                else:
                    return Response(
                        {
                            "success": False,
                            "message": "User not found ! please register",
                            "status": status.HTTP_404_NOT_FOUND,
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "success": False,
                        "message": "Mobile number and User ID is required",
                        "status": status.HTTP_400_BAD_REQUEST,
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


# verify otp
@permission_classes([AllowAny])
class VerifymobileOTPView(APIView):
    def post(self, request, format=None):
        try:
            otp = str(request.data.get("otp"))
            user_id = str(request.data.get("user_id"))
            if otp and user_id:
                user = User.objects.get(id__iexact=user_id)
                if user is None:
                    return Response(
                        {"success": False, "message": "User does not exist"},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                else:
                    if True:
                        # user.otp == otp:
                        user.is_verified = True
                        user.is_active = True
                        user.save()
                        login(request, user=user)
                        token, _ = Token.objects.get_or_create(user=user)
                        return Response(
                            {
                                "status": True,
                                "message": "Login Successfully",
                                "token": token.key,
                                "data": {
                                    "id": user.id,
                                    "username": user.username,
                                    "email": user.email,
                                    "mobile": user.mobile,
                                    "is_verified": user.is_verified,
                                },
                            },
                            status=status.HTTP_200_OK,
                        )
                    else:
                        return Response(
                            {"success": False, "message": "OTP does not match"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

            else:
                return Response(
                    {"success": False, "message": "mobile or OTP is missing"},
                    status=status.HTTP_403_FORBIDDEN,
                )

        except Exception as e:
            print(e)
            return Response(
                {
                    "success": False,
                    "message": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


# logout api view
@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = IsAuthenticated

    def post(self, request, format=None):
        try:
            logout(request)
            request.user.auth_token.delete()
            user = User.objects.get(id__iexact=request.user.id)
            user.is_verified = False
            user.otp = None
            user.save()
            return Response(
                {
                    "success": True,
                    "message": "Logout successfully",
                    "status": status.HTTP_200_OK,
                },
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "success": False,
                    "message": str(e),
                    "status": status.HTTP_400_BAD_REQUEST,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == "POST":
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get("old_password")):
                user.set_password(serializer.data.get("new_password"))
                user.save()
                update_session_auth_hash(
                    request, user
                )  # To update session after password change
                return Response(
                    {"message": "Password changed successfully."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {
                    "message": "Password changed successfully.",
                    "error": "Incorrect old password.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##############################################################

# # REGISTER
# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # LOGIN
# @api_view(['POST'])
# def user_login(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = None
#         if '@' in username:
#             try:
#                 user = User.objects.get(email=username)
#             except ObjectDoesNotExist:
#                 pass

#         if not user:
#             user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({'token': token.key}, status=status.HTTP_200_OK)

#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# LOGOUT
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             # Delete the user's token to logout
#             request.user.auth_token.delete()
#             return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

## Change Password
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def change_password(request):
#     if request.method == 'POST':
#         serializer = ChangePasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user = request.user
#             if user.check_password(serializer.data.get('old_password')):
#                 user.set_password(serializer.data.get('new_password'))
#                 user.save()
#                 update_session_auth_hash(request, user)  # To update session after password change
#                 return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
#             return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login with Email OTP
class passwordRecovery(APIView):
    def post(self, request):
        email = request.data.get("email", "")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User with this email does not exist."},
                status=status.HTTP_404_NOT_FOUND,
            )

        otp = generate_otp()
        user.otp = otp
        user.save()

        send_otp_email(email, otp)

        return Response(
            {"message": "OTP has been sent to your email."}, status=status.HTTP_200_OK
        )


# class ValidateOTP(APIView):
#     def post(self, request):
#         email = request.data.get('email', '')
#         otp = request.data.get('otp', '')

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_404_NOT_FOUND)

#         if user.otp == otp:
#             user.otp = None
#             user.save()

#             # Authenticate the user and create or get an authentication token
#             token, _ = Token.objects.get_or_create(user=user)

#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
