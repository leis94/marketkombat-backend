"""Product serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from vsbuy_backend.products.models.products import Product

class ProductModelSerializer(serializers.ModelSerializer):
    """Product model serializer."""

    class Meta:
        """Meta class."""
        model = Product
        fields = (
            'name',
        )
    
        read_only_fields = (
            'name',
        )
    
