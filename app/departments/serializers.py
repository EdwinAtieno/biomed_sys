from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (
    Department,
    Section,
)


class SectionSerializer(serializers.ModelSerializer):
    section_name = serializers.CharField(
        max_length=255,
        validators=[
            UniqueValidator(
                queryset=Section.objects.all(),
                message="Section with this name already exists",
                lookup="iexact",
            ),
        ],
    )
    specialization = serializers.CharField(max_length=255)

    class Meta:
        model = Section
        fields = ("id", "section_name", "specialization")


class DepartmentSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(max_length=255)
    department_location = serializers.CharField(max_length=255)
    building = serializers.CharField(max_length=255)
    sections = serializers.SlugRelatedField(
        many=True, slug_field="section_name", queryset=Section.objects.all()
    )

    class Meta:
        model = Department
        fields = (
            "id",
            "department_name",
            "department_location",
            "building",
            "sections",
        )
