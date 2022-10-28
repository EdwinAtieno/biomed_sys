from typing import Any

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.abstract import (
    IDModel,
    TimeStampedModel,
)
from app.users.validators import phone_number_validator

User = get_user_model()


class ContactPerson(IDModel, TimeStampedModel):
    contact_person_name = models.CharField(
        max_length=255, verbose_name=_("Contact Person Name")
    )
    contact_person_phone_number = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Phone Number"),
        validators=[
            phone_number_validator,
        ],
    )
    contact_person_email = models.EmailField(
        max_length=255, verbose_name=_("Contact Person Email")
    )
    contact_person_address = models.CharField(
        max_length=255, verbose_name=_("Contact Person Address")
    )

    def __str__(self) -> Any:
        return self.contact_person_name


class Supplier(TimeStampedModel, IDModel):
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.CharField(max_length=255)
    supplier_contact = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Phone Number",
        validators=[phone_number_validator],
    )
    contact_person = models.ForeignKey(ContactPerson, on_delete=models.CASCADE)
    supplier_email = models.EmailField(max_length=255)
    supplier_website = models.CharField(max_length=255)
    supplier_remarks = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text="User who created the supplier",
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    def __str__(self) -> Any:
        return self.supplier_name
