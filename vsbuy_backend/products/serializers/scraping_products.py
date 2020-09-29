"""Scraping Products serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from vsbuy_backend.products.models.scraping_products import ScrapingProduct

class ScrapingProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer."""

    class Meta:
        """Meta class."""
        model = ScrapingProduct
        fields = (
            'name',
            'price',
        )
    
        read_only_fields = (
            'name',
            'price',
        )
  