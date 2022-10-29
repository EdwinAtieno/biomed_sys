from typing import Any

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from app.abstract import (
    IDModel,
    TimeStampedModel,
)
from app.equipments.models import Equipment
from app.suppliers.models import Supplier

User = get_user_model()


class Repair(TimeStampedModel, IDModel):
    equipment = models.ForeignKey(Equipment, on_delete=models.PROTECT)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    repair_date = models.DateField(
        null=True, blank=True, verbose_name=_("update date and time")
    )
    repair_cost = models.DecimalField(max_digits=10, decimal_places=2)
    repair_description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        help_text="User who created the repair",
        null=True,
        blank=True,
    )

    def __str__(self) -> Any:
        return self.equipment.equipment_name
