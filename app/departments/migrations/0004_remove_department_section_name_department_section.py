# Generated by Django 4.1.2 on 2022-10-27 05:58

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):

    dependencies = [
        ("departments", "0003_department_section_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="department",
            name="section_name",
        ),
        migrations.AddField(
            model_name="department",
            name="section",
            field=models.ManyToManyField(
                related_name="section_set", to="departments.section"
            ),
        ),
    ]