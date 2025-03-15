from django.contrib.auth import logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes


# logout api view
@permission_classes([IsAuthenticated])
class LogOutAPIView(APIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            logout(request)

            print(request.headers)
            token_key = request.auth.key
            token = Token.objects.get(key=token_key)
            token.delete()

            # request.user.auth_token.delete()
            # user = User.objects.get(id__iexact=request.user.id)
            # user.save()
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
