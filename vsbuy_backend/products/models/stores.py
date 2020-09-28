"""Products mode. """

# Django
from django.db import models

# Utilities
from vsbuy_backend.utils.models import VSbuyModel

class Store(VSbuyModel):
    """Store model."""

    name = models.CharField(
        max_length=20,
    )

    logo = models.ImageField(
        'Store logo picture',
        upload_to = 'poroducts/pictures/market/',
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(
        default=True,
        help_text='Boolean field to get active a market'
    )


    def __str__(self):
        """Return Name"""
        return self.name