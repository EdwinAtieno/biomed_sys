# Generated by Django 4.1.2 on 2022-10-25 12:22

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                editable=False, primary_key=True, serialize=False
            ),
        ),
    ]