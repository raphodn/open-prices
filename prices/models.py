from django.db import models
from django.utils import timezone


class Price(models.Model):
    CURRENCY_EURO = "€"
    CURRENCY_CHOICES = [(CURRENCY_EURO, CURRENCY_EURO)]
    SOURCE_FORM = "FORM"
    SOURCE_API = "API"
    SOURCE_CHOICES = [(SOURCE_FORM, "Form"), (SOURCE_API, "API")]

    OFF_SOURCE_OFF = "OFF"
    OFF_SOURCE_OPF = "OPF"
    OFF_SOURCE_OPFF = "OPFF"
    OFF_SOURCE_OBF = "OBF"
    OFF_SOURCE_CHOICES = [
        (OFF_SOURCE_OFF, "OpenFoodFacts"),
        (OFF_SOURCE_OPF, "OpenProductFacts"),
        (OFF_SOURCE_OPFF, "OpenPetFoodFacts"),
        (OFF_SOURCE_OBF, "OpenBeautyFacts"),
    ]

    SERIALIZED_FIELDS = ["product_code", "price", "currency", "location_osm_id", "location_name", "date", "created"]
    READONLY_FIELDS = ["source", "created"]

    product_code = models.CharField(verbose_name="Product code")
    product_in_off = models.BooleanField(verbose_name="Product in OFF?", blank=True, null=True)
    product_off_db = models.CharField(verbose_name="Product OFF DB", choices=OFF_SOURCE_CHOICES, blank=True, null=True)
    product_off_name = models.CharField(verbose_name="Product name (OFF)", blank=True, null=True)

    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)
    currency = models.CharField(verbose_name="Currency", choices=CURRENCY_CHOICES, default=CURRENCY_EURO)

    location_osm_id = models.PositiveBigIntegerField(verbose_name="Location (OSM ID)")
    location_name = models.CharField(verbose_name="Location name", blank=True)

    date = models.DateField(verbose_name="Date")

    source = models.CharField(verbose_name="Currency", choices=SOURCE_CHOICES, default=SOURCE_FORM)

    created = models.DateTimeField(verbose_name="Creation date", default=timezone.now)

    class Meta:
        verbose_name = "Price"
        verbose_name_plural = "Prices"
