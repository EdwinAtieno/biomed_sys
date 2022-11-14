from typing import Any

from rest_framework import serializers

from app.equipments.models import Equipment
from app.repair.models import Repair
from app.suppliers.models import Supplier


class RepairSerializer(serializers.ModelSerializer):
    equipment = serializers.SlugRelatedField(
        slug_field="asset_number", queryset=Equipment.objects.all()
    )
    supplier = serializers.SlugRelatedField(
        slug_field="supplier_name", queryset=Supplier.objects.all()
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
