from django.urls import path

from app.users.views import (
    UserDetail,
    UserList,
)

urlpatterns = [
    path("users/", UserList.as_view(), name="user-list"),
    path("users/<str:pk>/", UserDetail.as_view(), name="user-detail"),
]
