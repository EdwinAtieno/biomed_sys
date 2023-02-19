from django.contrib import admin

from app.equipments.models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    model = Equipment
    list_display = (
        "asset_number",
        "equipment_name",
        "equipment_type",
        "department",
        "equipment_model",
        "equipment_serial_no",
        "status",
        "status_remarks",
        "supplier",
        "reported_on",
        "repaired_on",
        "created_at",
        "created_by",
    )
    ordering = ("asset_number",)
    readonly_fields = (
        "asset_number",
        "created_at",
        "created_by",
        "updated_at",
    )
    list_filter = (
        "equipment_name",
        "equipment_type",
        "department",
        "status",
    )

    search_fields = (
        "equipment_name",
        "equipment_type",
        "asset_number",
        "equipment_serial_no",
    )


admin.site.register(Equipment, EquipmentAdmin)
