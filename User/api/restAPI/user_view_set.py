# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from rest_framework import status
# from django.db import IntegrityError
# from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
# from rest_framework.authentication import (
#     TokenAuthentication,
#     SessionAuthentication,
#     BasicAuthentication,
# )
# from rest_framework.exceptions import PermissionDenied

# from Api.exceptions import (
#     SuccessResponse,
#     ValidationException,
#     DatabaseException,
#     ServerException,
# )
# from Api.views.serializers.registerSerializer import RegisterSerializer
# from App.messages import AuthMessages
# from User.models import User, Profile
# from User.utils.enums import USERS_TYPES
# from .serializers import (
#     ProfileSerializer,
#     UserDetailsSerializer,
#     PasswordSerializer,
# )
# import logging


# logger = logging.getLogger(__name__)


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
#     permission_classes = [IsAdminUser]
#     authentication_classes = [
#         TokenAuthentication,
#         SessionAuthentication,
#         BasicAuthentication,
#     ]

#     def get_serializer_class(self):
#         """Return appropriate serializer class based on action"""
#         if self.action == "retrieve_my_details":
#             return UserDetailsSerializer
#         elif self.action == "my_favorite_events":
#             return FavoriteEventSerializer
#         elif self.action == "my_interests":
#             return InterestCategorySerializer
#         return super().get_serializer_class()

#     def get_permissions(self):
#         """
#         Override to set different permissions based on action
#         """
#         if self.action == "register":
#             return [AllowAny()]  # Allow any for registration
#         elif self.action == "register_staff":
#             return [IsAdminUser()]  # Only admin can register staff
#         if self.action in [
#             "retrieve_my_details",
#             "my_favorite_events",
#             "my_interests",
#         ]:
#             return [IsAuthenticated()]
#         elif self.action == "register_staff":
#             return [IsAdminUser()]
#         return super().get_permissions()

#     # ... [keep all your existing actions: register, register_staff, register_superuser, set_password] ...

#     @action(detail=False, methods=["post"], permission_classes=[AllowAny])
#     def register(self, request):
#         """
#         Public registration endpoint for regular users and students
#         """
#         return self._register_user(
#             request, allowed_types=[USERS_TYPES.User, USERS_TYPES.Student]
#         )

#     @action(detail=False, methods=["post"], permission_classes=[IsAdminUser])
#     def register_staff(self, request):
#         """
#         Admin-only registration for staff, lecturers, and admins
#         """
#         return self._register_user(
#             request,
#             allowed_types=[USERS_TYPES.Staff, USERS_TYPES.Lecturer, USERS_TYPES.Admin],
#         )

#     @action(detail=False, methods=["post"], permission_classes=[IsAdminUser])
#     def register_superuser(self, request):
#         """
#         Superuser-only registration endpoint
#         """
#         # Only allow if requesting user is superuser
#         if not request.user.is_superuser:
#             return Response(
#                 {"detail": "Only superusers can create other superusers"},
#                 status=status.HTTP_403_FORBIDDEN,
#             )
#         return self._register_user(request, allowed_types=[USERS_TYPES.SuperUser])

#     def _register_user(self, request, allowed_types):
#         """
#         Internal method to handle user registration with type restrictions
#         """
#         serializer = self.get_serializer(data=request.data)

#         try:
#             # Validate input data
#             if not serializer.is_valid():
#                 raise ValidationException(
#                     errors=serializer.errors,
#                     message=AuthMessages.REGISTER_VALIDATION_ERROR,
#                 )

#             # Check if user type is allowed
#             user_type = serializer.validated_data.get("user_type", USERS_TYPES.User)
#             if user_type not in allowed_types:
#                 raise ValidationException(
#                     message=f"Registration as {user_type} is not allowed",
#                     status_code=status.HTTP_403_FORBIDDEN,
#                 )

#             # Create user
#             user = serializer.save()

#             # Handle profile data if provided
#             profile_data = request.data.get("profile")
#             if profile_data:
#                 profile_serializer = ProfileSerializer(
#                     data=profile_data, context={"user": user}
#                 )
#                 if profile_serializer.is_valid():
#                     profile_serializer.save()
#                 else:
#                     # If profile data is invalid, we still create the user but log the error
#                     logger.warning(
#                         "User created but profile data was invalid",
#                         extra={"errors": profile_serializer.errors},
#                     )

#             # Successful registration
#             logger.info(f"New user registered: {user.email}")
#             return SuccessResponse.create(
#                 data=serializer.data,
#                 message=AuthMessages.REGISTER_SUCCESS,
#                 status_code=status.HTTP_201_CREATED,
#             )

#         except IntegrityError as e:
#             logger.warning(
#                 f"Duplicate registration attempt for email: {serializer.initial_data.get('email')}",
#                 exc_info=True,
#                 extra={"email": serializer.initial_data.get("email"), "error": str(e)},
#             )
#             raise DatabaseException(
#                 message=AuthMessages.REGISTER_DUPLICATE,
#                 data={"email": serializer.initial_data.get("email")},
#                 status_code=status.HTTP_409_CONFLICT,
#             )

#         except ValidationException as e:
#             logger.warning(
#                 f"Registration validation failed: {str(e)}",
#                 exc_info=True,
#                 extra={
#                     "errors": e.errors,
#                     "email": serializer.initial_data.get("email"),
#                 },
#             )
#             raise

#         except Exception as e:
#             logger.critical(
#                 f"Unexpected registration error: {str(e)}",
#                 exc_info=True,
#                 extra={
#                     "email": serializer.initial_data.get("email"),
#                     "error_type": type(e).__name__,
#                 },
#             )
#             raise ServerException(
#                 message=f"{AuthMessages.REGISTER_FAILED}: {str(e)}",
#                 status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             )

#     # Add other actions like set_password, etc.
#     @action(detail=True, methods=["post"])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.validated_data["password"])
#             user.save()
#             return Response({"status": "password set"})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # Override default actions to prevent unwanted operations
#     def destroy(self, request, *args, **kwargs):
#         raise ValidationException(
#             message="Use dedicated delete action instead",
#             status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
#         )

#     @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
#     def retrieve_my_details(self, request):
#         """
#         Get authenticated user's own details
#         """
#         user = request.user
#         serializer = self.get_serializer(user)
#         return SuccessResponse.create(
#             data=serializer.data,
#             message="User details retrieved successfully",
#             status_code=status.HTTP_200_OK,
#         )

#     @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
#     def my_favorite_events(self, request):
#         """
#         Get authenticated user's favorite events
#         """
#         user = request.user
#         favorite_events = user.favorite_events.all()
#         serializer = self.get_serializer(favorite_events, many=True)
#         return SuccessResponse.create(
#             data=serializer.data,
#             message="Favorite events retrieved successfully",
#             status_code=status.HTTP_200_OK,
#         )

#     @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
#     def my_interests(self, request):
#         """
#         Get authenticated user's interesting notifiable categories
#         """
#         user = request.user
#         interests = user.interesting_notifiable_categories.all()
#         serializer = self.get_serializer(interests, many=True)
#         return SuccessResponse.create(
#             data=serializer.data,
#             message="Interests retrieved successfully",
#             status_code=status.HTTP_200_OK,
#         )

#     # Override default retrieve to prevent accessing other users' data
#     def retrieve(self, request, *args, **kwargs):
#         """
#         Override to prevent users from accessing other users' data
#         Admin users can still access any user's data
#         """
#         if not request.user.is_staff:
#             if str(request.user.pk) != kwargs.get("pk"):
#                 raise PermissionDenied("You can only access your own user data")
#         return super().retrieve(request, *args, **kwargs)
