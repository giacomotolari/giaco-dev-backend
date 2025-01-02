# Generated by Django 5.1.2 on 2025-01-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customercompany",
            name="size",
            field=models.CharField(
                choices=[
                    ("small", "Small"),
                    ("medium", "Medium"),
                    ("big", "Big"),
                    ("very-big", "Very big"),
                ],
                default="medium",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="employercompany",
            name="size",
            field=models.CharField(
                choices=[
                    ("small", "Small"),
                    ("medium", "Medium"),
                    ("big", "Big"),
                    ("very-big", "Very big"),
                ],
                default="medium",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="customercompany",
            name="company_type",
            field=models.CharField(
                choices=[
                    ("product-company", "Product Company"),
                    ("agency", "Agency"),
                    ("school", "School"),
                ],
                default="product-company",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="employercompany",
            name="company_type",
            field=models.CharField(
                choices=[
                    ("product-company", "Product Company"),
                    ("agency", "Agency"),
                    ("school", "School"),
                ],
                default="product-company",
                max_length=255,
            ),
        ),
    ]