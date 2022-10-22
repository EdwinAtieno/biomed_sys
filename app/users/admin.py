from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from app.users.models import RegistrationDetail

User = get_user_model()
# Register your models here.


class UserAdmin(DjangoUserAdmin):
    model = User
    list_display = (
        "id",
        "first_name",
        "middle_name",
        "last_name",
        "staff_number",
        "phone_number",
        "email",
        "created_at",
        "is_superuser",
    )

    ordering = ("first_name", "last_name")
    exclude = ("username", "date_joined")
    list_display_links = (
        "id",
        "staff_number",
    )
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "middle_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email")},
        ),
        ("Important dates", {"fields": ("last_login",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            "Personal info",
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "middle_name",
                    "password1",
                    "password2",
                ),
            },
        ),
        (
            "Contact info",
            {"fields": ("phone_number", "email")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                )
            },
        ),
    )


admin.site.register(User, UserAdmin)


class RegistrationDetailAdmin(admin.ModelAdmin):
    model = RegistrationDetail

    list_display = (
        "id",
        "user_phone_number",
        "user_name",
        "registered_by_phone_number",
        "registered_by_name",
        "registered_on",
    )

    ordering = (
        "registered_on",
        "user__phone_number",
        "registered_by__phone_number",
    )

    def user_phone_number(self, obj: RegistrationDetail) -> str:
        try:
            return obj.user.phone_number

        except Exception:
            return ""

    def registered_by_phone_number(self, obj: RegistrationDetail) -> str:
        try:
            return obj.registered_by.phone_number  # type: ignore

        except Exception:
            return ""

    def user_name(self, obj: RegistrationDetail) -> str:
        try:
            return f"{obj.user.first_name or ''} {obj.user.middle_name or ''} {obj.user.last_name or ''}"

        except Exception:
            return ""

    def registered_by_name(self, obj: RegistrationDetail) -> str:
        try:
            return f"{obj.registered_by.first_name or ''} {obj.registered_by.middle_name or ''} {obj.registered_by.last_name or ''}"  # type: ignore

        except Exception:
            return ""


admin.site.register(RegistrationDetail, RegistrationDetailAdmin)
