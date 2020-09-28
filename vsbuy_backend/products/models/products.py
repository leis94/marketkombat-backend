"""Products mode. """

# Django
from django.db import models

# Utilities
from vsbuy_backend.utils.models import VSbuyModel

class Product(VSbuyModel):
    """Products model."""

    name = models.CharField(
        max_length=20,
    )

    is_active = models.BooleanField(
        default=True,
        help_text='Boolean field to get active a product'
    )


    def __str__(self):
        """Return Name"""
        return self.name
