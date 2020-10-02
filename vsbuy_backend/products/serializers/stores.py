"""Product serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from vsbuy_backend.products.models.stores import Store

class StoreModelSerializer(serializers.ModelSerializer):
    """Store model serializer."""

    class Meta:
        """Meta class."""
        model = Store
        fields = (
            'name',
            'logo',
        )
    
        read_only_fields = (
            'name',
            'logo',
        )
