from typing import Any

from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView


class IsObjectOwnerOrAdmin(BasePermission):
    """
    Only grant permission to resource if one is owner or admin
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        return True

    def has_object_permission(
        self, request: Request, view: APIView, obj: Any
    ) -> bool:
        if obj.user == request.user or request.user.is_superuser:
            return True
        return False
