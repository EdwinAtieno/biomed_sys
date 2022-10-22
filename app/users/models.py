from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import (
    AbstractBaseUser,
    Group,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.abstract import (
    IDModel,
    TimeStampedModel,
)
from app.users.validators import (
    phone_number_validator,
    staff_number_validator,
)

# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(
        self, staff_number: str, password: str, **extra_fields: Any
    ) -> Any:
        """
        Create and save a user with the given staff_number and password.
        """
        if not staff_number:
            raise ValueError("The given staff_number must be set")
        user = self.model(staff_number=staff_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(
        self, staff_number: str, password: str, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(staff_number, password, **extra_fields)

    def create_superuser(
        self, staff_number: str, password: str, **extra_fields: Any
    ) -> Any:
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        superuser = self._create_user(staff_number, password, **extra_fields)
        group, _ = Group.objects.get_or_create(name="admin")
        superuser.groups.add(group)

        return superuser


class User(AbstractBaseUser, PermissionsMixin, IDModel, TimeStampedModel):
    first_name = models.CharField(max_length=255, verbose_name="First Name")
    middle_name = models.CharField(
        max_length=255, verbose_name="Middle Name", blank=True, null=True
    )
    last_name = models.CharField(max_length=255, verbose_name="Last Name")
    staff_number = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Staff Number",
        validators=[staff_number_validator],
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Phone Number",
        validators=[phone_number_validator],
    )
    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=255, verbose_name="Password")
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )

    is_available = models.BooleanField(
        _("available"),
        default=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "staff_number"

    def __str__(self) -> str:
        return self.staff_number


class RegistrationDetail(models.Model):
    """
    Displays who has registered a new user
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="registered_user",
        verbose_name=_("User"),
    )
    registered_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="registered_by",
        verbose_name=_("Registered By"),
    )
    registered_on = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Registered On")
    )

    def __str__(self) -> str:
        return f"{self.user} registered by {self.registered_by}"
