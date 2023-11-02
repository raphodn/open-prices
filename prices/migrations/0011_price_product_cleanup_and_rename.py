# Generated by Django 4.2.6 on 2023-11-02 11:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prices", "0010_price_product_migrate"),
    ]

    operations = [
        migrations.RenameField(
            model_name="price",
            old_name="product_code_link",
            new_name="product",
        ),
        migrations.RemoveField(
            model_name="price",
            name="product_in_off",
        ),
        migrations.RemoveField(
            model_name="price",
            name="product_off_db",
        ),
        migrations.RemoveField(
            model_name="price",
            name="product_off_image_url",
        ),
        migrations.RemoveField(
            model_name="price",
            name="product_off_name",
        ),
    ]
