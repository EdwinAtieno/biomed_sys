# Generated by Django 4.1.2 on 2022-11-05 19:32

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.CharField(
                editable=False,
                max_length=255,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]