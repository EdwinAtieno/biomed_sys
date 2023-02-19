# Generated by Django 4.1.2 on 2023-02-19 18:28

import django.db.models.deletion
from django.conf import settings
from django.db import (
    migrations,
    models,
)

import app.users.models
import app.users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
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
                    "id",
                    models.CharField(
                        editable=False,
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        max_length=255, verbose_name="First Name"
                    ),
                ),
                (
                    "middle_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Middle Name",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=255, verbose_name="Last Name"),
                ),
                (
                    "staff_number",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        validators=[
                            app.users.validators.staff_number_validator
                        ],
                        verbose_name="Staff Number",
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        validators=[
                            app.users.validators.phone_number_validator
                        ],
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "password",
                    models.CharField(max_length=255, verbose_name="Password"),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_available",
                    models.BooleanField(
                        default=True, verbose_name="available"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", app.users.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="RegistrationDetail",
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
                    "registered_on",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Registered On"
                    ),
                ),
                (
                    "registered_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="registered_by",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Registered By",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registered_user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
    ]
