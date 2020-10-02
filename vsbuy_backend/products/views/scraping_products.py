# Django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from vsbuy_backend.products.serializers.scraping_products import (ScrapingProductModelSerializer,
CreateScrapingProductSerializer,
ScrapingProductNoUserSerializer,)

# Models
from vsbuy_backend.products.models.scraping_products import ScrapingProduct
from vsbuy_backend.products.models.products import Product


class ScrapingProductViewSet(mixins.CreateModelMixin,
                             mixins.ListModelMixin,
                             viewsets.GenericViewSet):

    search_fields = ['product__name', 'name', ]
    filter_backends = (filters.SearchFilter, OrderingFilter)

    queryset = ScrapingProduct.objects.all()
    serializer_class = ScrapingProductModelSerializer

    ordering = ('price',)


    def get_serializer_class(self):
        if self.request.user.is_anonymous:
            return ScrapingProductNoUserSerializer
        else:
            return ScrapingProductModelSerializer


    def create(self, request, *args, **kwargs):
        """Handle creation from invitation code."""
        import pdb; pdb.set_trace()
        serializer = CreateScrapingProductSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        scrap_product = serializer.save()

        data = self.get_serializer(scrap_product).data
        return Response(data, status=status.HTTP_201_CREATED)

