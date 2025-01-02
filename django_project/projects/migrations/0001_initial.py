# Generated by Django 5.1.2 on 2025-01-02 22:38

import django.db.models.deletion
import multiselectfield.db.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("companies", "0003_alter_customercompany_company_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonalProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("planned", "Planned"),
                            ("in-progress", "In Progress"),
                            ("completed", "Completed"),
                            ("archived", "Archived"),
                            ("paused", "Paused"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("big", "Big"),
                            ("very big", "Very Big"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "runs_on",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("web", "Web"),
                            ("desktop", "Desktop"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "categories",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("e-commerce", "E Commerce"),
                            ("community", "Community"),
                            ("game", "Game"),
                            ("portfolio", "Portfolio"),
                            ("blog", "Blog"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("urls", models.JSONField(blank=True, null=True)),
                ("goals", models.JSONField(blank=True, null=True)),
                ("extra_infos", models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamOpenSourceProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("planned", "Planned"),
                            ("in-progress", "In Progress"),
                            ("completed", "Completed"),
                            ("archived", "Archived"),
                            ("paused", "Paused"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("big", "Big"),
                            ("very big", "Very Big"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "runs_on",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("web", "Web"),
                            ("desktop", "Desktop"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "categories",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("e-commerce", "E Commerce"),
                            ("community", "Community"),
                            ("game", "Game"),
                            ("portfolio", "Portfolio"),
                            ("blog", "Blog"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("urls", models.JSONField(blank=True, null=True)),
                ("goals", models.JSONField(blank=True, null=True)),
                ("extra_infos", models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TeamPrivateProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("planned", "Planned"),
                            ("in-progress", "In Progress"),
                            ("completed", "Completed"),
                            ("archived", "Archived"),
                            ("paused", "Paused"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("big", "Big"),
                            ("very big", "Very Big"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "runs_on",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("web", "Web"),
                            ("desktop", "Desktop"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "categories",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("e-commerce", "E Commerce"),
                            ("community", "Community"),
                            ("game", "Game"),
                            ("portfolio", "Portfolio"),
                            ("blog", "Blog"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("urls", models.JSONField(blank=True, null=True)),
                ("goals", models.JSONField(blank=True, null=True)),
                ("extra_infos", models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AsEmployeeProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("planned", "Planned"),
                            ("in-progress", "In Progress"),
                            ("completed", "Completed"),
                            ("archived", "Archived"),
                            ("paused", "Paused"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("big", "Big"),
                            ("very big", "Very Big"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "runs_on",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("web", "Web"),
                            ("desktop", "Desktop"),
                            ("ios", "Ios"),
                            ("android", "Android"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "categories",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("e-commerce", "E Commerce"),
                            ("community", "Community"),
                            ("game", "Game"),
                            ("portfolio", "Portfolio"),
                            ("blog", "Blog"),
                            ("other", "Other"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("urls", models.JSONField(blank=True, null=True)),
                ("goals", models.JSONField(blank=True, null=True)),
                ("extra_infos", models.TextField(blank=True, max_length=255, null=True)),
                (
                    "customer_companies",
                    models.ManyToManyField(related_name="projects", to="companies.customercompany"),
                ),
                (
                    "employed_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="companies.employercompany"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]