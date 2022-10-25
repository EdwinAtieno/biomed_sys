from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    ChangePassword,
    MyTokenObtainPairView,
)

urlpatterns = [
    path("sign-in/", MyTokenObtainPairView.as_view(), name="sign-in"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path(
        "auth/change-password/<str:pk>/",
        ChangePassword.as_view(),
        name="change-password",
    ),
]
