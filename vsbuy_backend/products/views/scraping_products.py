# Django REST Framework
from rest_framework import viewsets, mixins
# from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

# Serializers
from vsbuy_backend.products.serializers.scraping_products import ScrapingProductModelSerializer

# Models
from vsbuy_backend.products.models.scraping_products import ScrapingProduct
from vsbuy_backend.products.models.products import Product


class ScrapFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    product__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = ScrapingProduct
        fields = ('name','product__name')


class ScrapingProductViewSet(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    queryset = ScrapingProduct.objects.all()
    serializer_class = ScrapingProductModelSerializer

    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    filterset_class = ScrapFilter
    search_fields = ('name','product__name')
    ordering = ('price',)

