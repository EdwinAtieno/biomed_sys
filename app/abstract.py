from typing import Any
from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


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
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True

    def save(self, *args: Any, **kwargs: Any) -> Any:
        if not self.id:
            is_unique = False
            while not is_unique:
                id = uuid4().hex
                is_unique = not self.__class__.objects.filter(
                    id=self.id
                ).exists()
            self.id = id
        return super().save(*args, **kwargs)
