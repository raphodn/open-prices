# Generated by Django 4.2.6 on 2023-11-02 10:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "code",
                    models.CharField(editable=False, primary_key=True, serialize=False, verbose_name="Product code"),
                ),
                ("in_off", models.BooleanField(blank=True, null=True, verbose_name="Product in OFF?")),
                (
                    "off_db",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("OFF", "OpenFoodFacts"),
                            ("OPF", "OpenProductFacts"),
                            ("OPFF", "OpenPetFoodFacts"),
                            ("OBF", "OpenBeautyFacts"),
                        ],
                        null=True,
                        verbose_name="Product OFF DB",
                    ),
                ),
                ("off_name", models.CharField(blank=True, null=True, verbose_name="Product name (OFF)")),
                ("off_image_url", models.URLField(blank=True, null=True, verbose_name="Product image URL (OFF)")),
                ("created", models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Last update date")),
            ],
            options={
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
    ]
