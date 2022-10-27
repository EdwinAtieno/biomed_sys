from django.urls import path

from .views import (
    DepartmentDetail,
    DepartmentList,
    SectionDetail,
    SectionList,
)

urlpatterns = [
    path("departments/", DepartmentList.as_view(), name="department-list"),
    path(
        "departments/<str:pk>/",
        DepartmentDetail.as_view(),
        name="department-detail",
    ),
    path("sections/", SectionList.as_view(), name="section-list"),
    path("sections/<str:pk>/", SectionDetail.as_view(), name="section-detail"),
]
