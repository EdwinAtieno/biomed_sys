from typing import Any

from rest_framework import serializers

from app.repair.models import Repair


class RepairSerializer(serializers.ModelSerializer):
    equipment = serializers.CharField(
        source="Equipment.equipment_name", max_length=255
    )
    supplier = serializers.CharField(
        source="Supplier.supplier_name", max_length=255
    )
    repair_date = serializers.DateField(allow_null=True)
    repair_cost = serializers.DecimalField(max_digits=10, decimal_places=2)
    repair_description = serializers.CharField(max_length=255)

    class Meta:
        model = Repair
        fields = (
            "id",
            "equipment",
            "supplier",
            "repair_date",
            "repair_cost",
            "repair_description",
        )
        read_only_fields = ("id",)

    def create(self, validated_data: Any) -> Any:
        user = self.context["request"].user
        validated_data["created_by"] = user
        repair = Repair.objects.create(**validated_data)
        return repair
