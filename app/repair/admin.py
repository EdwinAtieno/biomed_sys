from django.contrib import admin

from app.repair.models import Repair


class RepairAdmin(admin.ModelAdmin):
    model = Repair
    list_display = (
        "equipment",
        "supplier",
        "repair_date",
        "repair_cost",
        "repair_description",
        "created_by",
    )
    ordering = ("equipment",)
    readonly_fields = ("created_by",)
    list_filter = (
        "equipment",
        "supplier",
        "repair_date",
        "created_by",
    )

    search_fields = (
        "equipment",
        "supplier",
        "created_by",
    )


admin.site.register(Repair, RepairAdmin)
