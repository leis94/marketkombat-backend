"""Store views."""

# Django REST Framework
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated
from vsbuy_backend.products.permissions import IsSuperUser

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Serializers
from vsbuy_backend.products.serializers.stores import StoreModelSerializer

# Models
from vsbuy_backend.products.models.stores import Store

class StoreViewSet(mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    """Product view set."""

    queryset = Store.objects.filter(is_active=True)
    serializer_class = StoreModelSerializer
    lookup_field = 'name'

    # Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('name')
    ordering = ('id')
