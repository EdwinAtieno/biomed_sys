from typing import Any

from rest_framework.permissions import (
    SAFE_METHODS,
    BasePermission,
)
from rest_framework.request import Request
from rest_framework.views import APIView


class IsBioMedorAdmin(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        return True

    def has_object_permission(
        self, request: Request, view: APIView, obj: Any
    ) -> bool:
        if (
            request.user.groups.filter(name="biomed").exists()  # type: ignore[union-attr]
            and request.method in SAFE_METHODS
        ):
            return True

        if obj.user == request.user or request.user.is_superuser:
            return True
        return False
