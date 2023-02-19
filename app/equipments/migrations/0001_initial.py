# Generated by Django 4.1.2 on 2022-10-28 19:09

import django.db.models.deletion
from django.conf import settings
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("departments", "0005_rename_section_department_sections"),
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="created at"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="updated at"
                    ),
                ),
                (
                    "asset_number",
                    models.CharField(
                        editable=False,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("equipment_name", models.CharField(max_length=255)),
                (
                    "equipment_serial_no",
                    models.CharField(max_length=255, unique=True),
                ),
                ("equipment_type", models.CharField(max_length=255)),
                (
                    "equipment_model",
                    models.CharField(
                        choices=[
                            ("lease", "lease"),
                            ("outright purchase", "outright purchase"),
                            ("placement", "placement"),
                        ],
                        default="lease",
                        max_length=255,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "active"),
                            ("broken", "broken"),
                            ("repaired", "repaired"),
                            ("out of service", "out of service"),
                            ("in maintenance", "in maintenance"),
                        ],
                        default="active",
                        max_length=255,
                    ),
                ),
                ("status_remarks", models.TextField(blank=True, null=True)),
                (
                    "reported_on",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="update date and time",
                    ),
                ),
                (
                    "repaired_on",
                    models.DateTimeField(
                        blank=True,
                        null=True,
                        verbose_name="update date and time",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        help_text="User who created the equipment",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="departments.department",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        help_text="Supplier",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="suppliers.supplier",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
