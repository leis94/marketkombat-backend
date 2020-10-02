"""Product views."""

# Django REST Framework
from rest_framework import viewsets, mixins

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from vsbuy_backend.products.serializers.products import ProductModelSerializer

# Models
from vsbuy_backend.products.models.products import Product

class ProductViewSet(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """Product view set."""

    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductModelSerializer
    lookup_field = 'name'

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name')
    ordering = ('id')


