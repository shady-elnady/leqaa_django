from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_fcm_token(request):
    token = request.data.get("fcm_token")
    if not token:
        return Response(
            {"error": "FCM token is required."}, status=status.HTTP_400_BAD_REQUEST
        )

    user = request.user
    user.fcm_token = token
    user.save()
    return Response(
        {"message": "FCM token updated successfully."}, status=status.HTTP_200_OK
    )
