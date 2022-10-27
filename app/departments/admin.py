from django.contrib import admin

from .models import (
    Department,
    Section,
)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department
    list_display = (
        "id",
        "department_name",
        "department_location",
        "building",
        "updated_at",
        "get_sections",
    )
    ordering = ("department_name",)
    readonly_fields = ("updated_at",)
    list_filter = (
        "department_name",
        "department_location",
    )

    search_fields = (
        "department_name",
        "department_location",
    )


admin.site.register(Department, DepartmentAdmin)


class SectionAdmin(admin.ModelAdmin):
    model = Section
    list_display = (
        "id",
        "section_name",
        "specialization",
        "updated_at",
    )
    ordering = ("section_name",)
    readonly_fields = ("updated_at",)
    list_filter = (
        "section_name",
        "specialization",
    )

    search_fields = (
        "section_name",
        "specialization",
    )


admin.site.register(Section, SectionAdmin)
