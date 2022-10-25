from typing import Any

from django.contrib.auth import (
    authenticate,
    get_user_model,
)
from rest_framework import (
    exceptions,
    serializers,
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):  # type: ignore
    @classmethod
    def get_token(cls, user: Any) -> Any:
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["staff_number"] = user.staff_number
        token["email"] = user.email
        token["phone_number"] = user.phone_number
        token["roles"] = list(user.groups.values_list("name", flat=True))

        return token


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(max_length=6, write_only=True)
    password = serializers.CharField(max_length=6, write_only=True)
    confirm_password = serializers.CharField(max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ("current_password", "password", "confirm_password")

    def validate(self, data: Any) -> Any:
        try:
            int(data["password"])
        except ValueError:
            raise exceptions.ValidationError(
                {"password": "Password must be a 8 digit password"}
            )

        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"detail": "Password must match confirm password"}
            )

        user = self.context["request"].user

        if not authenticate(
            staff_number=user.staff_number,
            password=data["current_password"],
        ):
            raise exceptions.AuthenticationFailed("Invalid password")

        return data

    def update(self, instance: Any, validated_data: Any) -> Any:
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
