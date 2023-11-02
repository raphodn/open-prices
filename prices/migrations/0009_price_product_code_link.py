# Generated by Django 4.2.6 on 2023-11-02 11:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
        ("prices", "0008_rename_location_name_price_location_osm_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="product_code_link",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prices",
                to="products.product",
                verbose_name="Product code",
            ),
        ),
    ]
