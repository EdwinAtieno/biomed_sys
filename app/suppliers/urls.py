from django.urls import path

from app.suppliers.views import (
    ContactPersonDetail,
    ContactPersonList,
    SupplierDetail,
    SupplierList,
)

urlpatterns = [
    path("suppliers/", SupplierList.as_view(), name="supplier-list"),
    path(
        "suppliers/<str:pk>/", SupplierDetail.as_view(), name="supplier-detail"
    ),
    path(
        "contactpersons/",
        ContactPersonList.as_view(),
        name="contactperson-list",
    ),
    path(
        "contactpersons/<str:pk>/",
        ContactPersonDetail.as_view(),
        name="contactperson-detail",
    ),
]
