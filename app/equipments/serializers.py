from typing import Any

from django.utils import timezone
from rest_framework import serializers

from app.departments.models import Department
from app.equipments.constant import (
    EQUIPMENT_STATUS,
    EQUIPMENT_TYPE,
)
from app.equipments.models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=EQUIPMENT_STATUS, default="active"
    )
    equipment_type = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True
    )
    equipment_model = serializers.ChoiceField(
        choices=EQUIPMENT_TYPE, default="lease"
    )
    department = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all()
    )
    asset_number = serializers.CharField(read_only=True)
    equipment_name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    status_remarks = serializers.CharField(
        max_length=255, allow_blank=True, allow_null=True
    )
    equipment_serial_no = serializers.CharField(max_length=255)

    class Meta:
        model = Equipment
        fields = (
            "asset_number",
            "equipment_name",
            "equipment_type",
            "equipment_model",
            "equipment_serial_no",
            "description",
            "status",
            "status_remarks",
            "department",
            "supplier",
            "reported_on",
            "repaired_on",
            "created_by",
        )
        read_only_fields = ("asset_number", "created_by")

    def validate_asset_number(self, asset_number: Any) -> Any:
        if not Equipment.objects.filter(asset_number=asset_number).exists():
            return asset_number
        raise serializers.ValidationError("This asset number already exists")

    def validate_equipment_serial_no(self, equipment_serial_no: Any) -> Any:
        if not Equipment.objects.filter(
            equipment_serial_no=equipment_serial_no
        ).exists():
            return equipment_serial_no
        raise serializers.ValidationError("This serial number already exists")

    def create(self, validated_data: Any) -> Any:
        user = self.context["request"].user
        validated_data["created_by"] = user
        equipment = Equipment.objects.create(**validated_data)
        return equipment


class EquipmentStatusSerializer(serializers.ModelSerializer):
    asset_number = serializers.CharField(read_only=True)

    class Meta:
        model = Equipment
        fields = ("asset_number", "status", "status_remarks")

    def update(self, instance: Any, validated_data: Any) -> Any:
        instance.status = validated_data.get("status", instance.status)
        instance.status_remarks = validated_data.get(
            "status_remarks", instance.status_remarks
        )
        instance.reported_on = None
        instance.repaired_on = None

        if (
            validated_data.get("status") == "broken"
            or validated_data.get("status") == "out of service"
            or validated_data.get("status") == "in maintenance"
        ):
            instance.reported_on = timezone.now()

        if validated_data.get("status") == "repaired":
            instance.repaired_on = timezone.now()

        instance.save()
        return instance
