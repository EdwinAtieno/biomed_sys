from django.urls import path

from app.repair.views import (
    RepairDetail,
    RepairList,
)

urlpatterns = [
    path("repair/", RepairList.as_view(), name="repair-list-create"),
    path(
        "repair/<str:pk>/",
        RepairDetail.as_view(),
        name="repair-retrieve-update-destroy",
    ),
]
