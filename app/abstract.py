from typing import Any
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

from utils import (
    generate_asset_number,
    generate_number,
)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        _("created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(
        _("updated at"), auto_now=True, editable=False
    )

    class Meta:
        """
        We put abstract=True in the Meta class so that the model will not be used to create any database table.
        Instead, when it is used as a base class for other models, its fields will be added to those of the child class.
        """

        abstract = True
        ordering = (
            "-created_at",
            "-updated_at",
        )


class IDModel(models.Model):
    id = models.UUIDField(primary_key=True, max_length=255, editable=False)

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> Any:
        if not self.id:
            is_unique = False
            while not is_unique:
                id = uuid4().hex
                is_unique = not self.__class__.objects.filter(id=id).exists()
            self.id = id
        return super().save(*args, **kwargs)


class IntegerIDModel(models.Model):
    """
    An abstract base class that allows us to generate a unique integer id for each model.
    """

    id = models.CharField(primary_key=True, max_length=255, editable=False)

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> Any:
        if not self.id:
            is_unique = False
            while not is_unique:
                id = generate_number(num_digits=12)
                is_unique = not self.__class__.objects.filter(id=id).exists()

            self.id = id
        return super().save(*args, **kwargs)


class EquipmentAssetNumberModel(models.Model):
    """
    An abstract base class that allows us to generate a unique integer id for each model.
    """

    asset_number = models.CharField(
        primary_key=True,
        max_length=255,
        editable=False,
    )

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> Any:
        if not self.asset_number:
            is_unique = False
            while not is_unique:
                asset_number = generate_asset_number(num_digits=5)
                is_unique = not self.__class__.objects.filter(
                    asset_number=asset_number
                ).exists()

            self.asset_number = asset_number
        return super().save(*args, **kwargs)


class SoftDeleteModel(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def delete(self, *args: Any, **kwargs: Any) -> Any:
        self.is_active = False
        self.save()

    def hard_delete(self, *args: Any, **kwargs: Any) -> Any:
        super().delete(*args, **kwargs)
