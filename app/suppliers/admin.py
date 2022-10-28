from django.contrib import admin

from app.suppliers.models import (
    ContactPerson,
    Supplier,
)


class ContactPersonAdmin(admin.ModelAdmin):
    model = ContactPerson
    list_display = (
        "id",
        "contact_person_name",
        "contact_person_email",
        "contact_person_phone_number",
        "contact_person_address",
    )
    ordering = ("contact_person_name",)
    readonly_fields = ("id",)

    search_fields = (
        "contact_person_name",
        "contact_person_email",
        "contact_person_phone_number",
    )


admin.site.register(ContactPerson, ContactPersonAdmin)


class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    list_display = (
        "id",
        "supplier_name",
        "supplier_address",
        "supplier_contact",
        "supplier_email",
        "supplier_website",
        "supplier_remarks",
    )
    ordering = ("supplier_name",)
    readonly_fields = ("id",)

    search_fields = (
        "supplier_name",
        "supplier_address",
        "supplier_contact",
        "supplier_email",
        "supplier_website",
        "supplier_remarks",
    )


admin.site.register(Supplier, SupplierAdmin)
