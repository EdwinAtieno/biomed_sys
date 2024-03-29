# Generated by Django 4.1.2 on 2023-02-19 18:37

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
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
                    "section_name",
                    models.CharField(max_length=255, unique=True),
                ),
                ("specialization", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("-created_at", "-updated_at"),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("department_name", models.CharField(max_length=255)),
                ("department_location", models.CharField(max_length=255)),
                ("building", models.CharField(max_length=255)),
                (
                    "sections",
                    models.ManyToManyField(
                        related_name="section_set", to="departments.section"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
