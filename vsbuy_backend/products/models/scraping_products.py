"""Scraping Products models. """

# Django
from django.db import models

# Utilities
from vsbuy_backend.utils.models import VSbuyModel


class ScrapingProduct(VSbuyModel):
    """Scraping Products model."""

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text='Relationship from which product was scraped'
    )

    store = models.ForeignKey(
        'products.Store',
        on_delete=models.CASCADE,
        help_text='Relationship from which store was scraped'
    )

    name = models.CharField(max_length=255)

    picture = models.ImageField(
        'Store the image of the product scraped',
        upload_to='products/pictures/market/',
        null=True,
        blank=True,
    )

    url = models.URLField(max_length=300)
    price = models.DecimalField(max_digits=19, decimal_places=10)

    rank = models.PositiveIntegerField(null=True, blank=True)

    is_active = models.BooleanField(
        default=True,
        help_text='Boolean field to get active a market'
    )

    def __str__(self):
        """Return Name"""
        return self.name
