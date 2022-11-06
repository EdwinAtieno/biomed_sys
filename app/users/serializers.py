from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from app.users.constants import USER_GROUPS
from app.users.validators import (
    phone_number_validator,
    staff_number_validator,
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    middle_name = serializers.CharField(
        max_length=255, allow_blank=True, required=False
    )
    last_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(
        max_length=20,
        validators=[
            phone_number_validator,
            UniqueValidator(
                queryset=User.objects.all(),
                message="This phone number already exists",
                lookup="iexact",
            ),
        ],
    )
    staff_number = serializers.CharField(
        max_length=255,
        validators=[
            staff_number_validator,
            UniqueValidator(
                queryset=User.objects.all(),
                message="This staff number already exists",
                lookup="iexact",
            ),
        ],
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="This email already exists",
                lookup="iexact",
            ),
        ],
    )
    password = serializers.CharField(min_length=8, write_only=True)
    roles = serializers.SerializerMethodField()
    role = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "role",
            "middle_name",
            "roles",
            "phone_number",
            "staff_number",
            "password",
        )
        read_only_fields = ("id", "roles")

    def get_roles(self, obj: Any) -> Any:
        return list(obj.groups.values_list("name", flat=True))

    def validate_phone_number(self, phone_number: Any) -> Any:
        if not User.objects.filter(phone_number=phone_number).exists():
            return phone_number
        raise serializers.ValidationError("This phone number already exists")

    def validate_staff_number(self, staff_number: Any) -> Any:
        if not User.objects.filter(staff_number=staff_number).exists():
            return staff_number
        raise serializers.ValidationError("This staff number already exists")

    def validate_email(self, email: Any) -> Any:
        if not User.objects.filter(email=email).exists():
            return email
        raise serializers.ValidationError("This email already exists")

    def validate_role(self, role: Any) -> Any:
        """
        Ensure that the role provided is valid
        """

        user = self.context["request"].user
        role = role.lower()
        if role in USER_GROUPS:
            if role == "admin":
                if not user.is_superuser:
                    raise serializers.ValidationError(
                        "You do not have the permission to create an admin user"
                    )
            return role
        raise serializers.ValidationError(
            f"Invalid role. Only { ', '.join(USER_GROUPS)} are allowed"
        )

    def create(self, validated_data: Any) -> Any:
        """
        Create a new user with the provided data
        """
        role = validated_data.pop("role")
        user = User.objects.create_user(**validated_data)
        group, _ = Group.objects.get_or_create(name=role)
        user.groups.add(group)

        return user
