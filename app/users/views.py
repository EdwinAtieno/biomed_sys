from typing import Any

from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from rest_framework import (
    exceptions,
    generics,
)
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
)
from rest_framework.request import Request
from rest_framework.response import Response

from app.users.permissions import IsObjectOwnerOrAdmin
from app.users.serializers import UserSerializer

User = get_user_model()


class UsersList(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer: Any) -> None:
        serializer.save()


class UserList(generics.ListAPIView):
    """
    List all users, or create a new user by admin.
    """

    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """

    queryset = User.objects.prefetch_related("groups").all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsObjectOwnerOrAdmin)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """
        User must authenticate before deleting their account
        """
        user = request.user
        data = request.data
        authenticated_user = authenticate(
            staff_number=user.staff_number, password=data["password"]  # type: ignore[union-attr]
        )
        if authenticated_user is not None or user.is_superuser:
            return self.destroy(request, *args, **kwargs)

        raise exceptions.AuthenticationFailed({"detail": "Invalid password"})
