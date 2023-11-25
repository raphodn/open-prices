# Generated by Django 4.2.6 on 2023-11-02 12:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("osm_id", models.PositiveBigIntegerField(verbose_name="ID (OSM)")),
                (
                    "osm_type",
                    models.CharField(
                        blank=True,
                        choices=[("NODE", "Node"), ("WAY", "Way"), ("RELATION", "Relation")],
                        null=True,
                        verbose_name="Type (OSM)",
                    ),
                ),
                ("osm_display_name", models.CharField(blank=True, null=True, verbose_name="Display name (OSM)")),
                (
                    "osm_lat",
                    models.DecimalField(
                        blank=True, decimal_places=7, max_digits=11, null=True, verbose_name="Latitude (OSM)"
                    ),
                ),
                (
                    "osm_lon",
                    models.DecimalField(
                        blank=True, decimal_places=7, max_digits=11, null=True, verbose_name="Longitude (OSM)"
                    ),
                ),
                ("created", models.DateTimeField(default=django.utils.timezone.now, verbose_name="Creation date")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Last update date")),
            ],
            options={
                "verbose_name": "Location",
                "verbose_name_plural": "Locations",
                "unique_together": {("osm_id", "osm_type")},
            },
        ),
    ]