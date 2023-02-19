from typing import Any

from django.db import models

from app.abstract import (
    IntegerIDModel,
    TimeStampedModel,
)


class Section(TimeStampedModel):
    section_name = models.CharField(max_length=255, unique=True)
    specialization = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.section_name


class Department(IntegerIDModel, TimeStampedModel):
    department_name = models.CharField(max_length=255)
    department_location = models.CharField(max_length=255)
    building = models.CharField(max_length=255)
    sections = models.ManyToManyField(Section, related_name="section_set")

    def __str__(self) -> str:
        return self.department_name

    def get_sections(self) -> Any:
        return "\n".join([p.section_name for p in self.sections.all()])
