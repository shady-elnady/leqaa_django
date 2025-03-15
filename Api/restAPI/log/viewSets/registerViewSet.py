from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status, serializers
from django.utils.translation import gettext_lazy as _

from User.models import User
from ..serializers.registerSerializer import RegisterSerializer

# Create your views here.


class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)  # noqa: F841
        return Response(
            {
                "data": serializer.data,
                "success": True,
                "message": "User created successfully. You Can LogIN now",
                "status": status.HTTP_201_CREATED,
            },
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        raise serializers.ValidationError(
            _("This URL is Post Request To Register "),
        )
