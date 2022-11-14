from typing import Any

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.abstract import (
    EquipmentAssetNumberModel,
    TimeStampedModel,
)
from app.departments.models import Department
from app.equipments.constant import (
    EQUIPMENT_STATUS,
    EQUIPMENT_TYPE,
)
from app.suppliers.models import Supplier

User = get_user_model()


class Equipment(EquipmentAssetNumberModel, TimeStampedModel):
    equipment_name = models.CharField(max_length=255)
    equipment_serial_no = models.CharField(max_length=255, unique=True)
    equipment_type = models.CharField(max_length=255)
    equipment_model = models.CharField(
        max_length=255, default="lease", choices=EQUIPMENT_TYPE
    )
    description = models.TextField()
    status = models.CharField(
        max_length=255, default="active", choices=EQUIPMENT_STATUS
    )
    status_remarks = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    reported_on = models.DateTimeField(
        null=True, blank=True, verbose_name=_("update date and time")
    )
    transfer_to = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text="User who created the equipment",
        null=True,
        blank=True,
    )
    repaired_on = models.DateTimeField(
        null=True, blank=True, verbose_name=_("update date and time")
    )

    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, help_text="Supplier"
    )

    def __str__(self) -> Any:
        return self.equipment_name
