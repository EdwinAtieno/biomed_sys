from django.urls import path

from app.equipments.views import (
    EquipmentDetail,
    EquipmentList,
    EquipmentStatusUpdate,
)

urlpatterns = [
    path("equipments/", EquipmentList.as_view(), name="equipment-list"),
    path(
        "equipments/<str:pk>/",
        EquipmentDetail.as_view(),
        name="equipment-detail",
    ),
    path(
        "equipments/<str:pk>/status/",
        EquipmentStatusUpdate.as_view(),
        name="equipment-status-update",
    ),
]
