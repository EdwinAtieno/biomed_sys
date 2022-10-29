"""nh_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import (
    include,
    path,
)
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

admin.site.site_header = "NHS Administration"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("app.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="NHS API",
        default_version="v1",
        description="NHS API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

if settings.DEBUG:
    urlpatterns += [
        path(
            "docs/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
        path(
            "docs/swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
    ]
