from typing import Any

from rest_framework import serializers

from app.suppliers.models import (
    ContactPerson,
    Supplier,
)


class ContactPersonSerializer(serializers.ModelSerializer):
    contact_person_name = serializers.CharField(max_length=255)
    contact_person_email = serializers.EmailField(max_length=255)
    contact_person_phone_number = serializers.CharField(max_length=255)
    contact_person_address = serializers.CharField(max_length=255)

    class Meta:
        model = ContactPerson
        fields = (
            "id",
            "contact_person_name",
            "contact_person_email",
            "contact_person_phone_number",
            "contact_person_address",
        )
        read_only_fields = ("id", "created_by")

    def validate_email(self, contact_person_email: Any) -> Any:
        if not ContactPerson.objects.filter(
            contact_person_email=contact_person_email
        ).exists():
            return contact_person_email
        raise serializers.ValidationError("This email already exists")

    def validate_phone_number(self, contact_person_phone_number: Any) -> Any:
        if not ContactPerson.objects.filter(
            contact_person_phone_number=contact_person_phone_number
        ).exists():
            return contact_person_phone_number
        raise serializers.ValidationError("This phone number already exists")


class SupplierSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(max_length=255)
    supplier_address = serializers.CharField(max_length=255)
    supplier_contact = serializers.CharField(max_length=255)
    supplier_email = serializers.EmailField(max_length=255)
    supplier_website = serializers.CharField(max_length=255, allow_blank=True)
    supplier_remarks = serializers.CharField(max_length=255)
    contact_person = serializers.SerializerMethodField()

    class Meta:
        model = Supplier
        fields = (
            "id",
            "supplier_name",
            "supplier_address",
            "supplier_contact",
            "supplier_email",
            "supplier_website",
            "supplier_remarks",
            "created_by",
            "contact_person",
        )
        read_only_fields = ("id", "created_by")

    def validate_email(self, supplier_email: Any) -> Any:
        if not Supplier.objects.filter(supplier_email=supplier_email).exists():
            return supplier_email
        raise serializers.ValidationError("This email already exists")

    def validate_phone_number(self, supplier_contact: Any) -> Any:
        if not Supplier.objects.filter(
            supplier_contact=supplier_contact
        ).exists():
            return supplier_contact
        raise serializers.ValidationError("This phone number already exists")

    def create(self, validated_data: Any) -> Any:
        user = self.context["request"].user
        validated_data["created_by"] = user
        supplier = Supplier.objects.create(**validated_data)
        return supplier
