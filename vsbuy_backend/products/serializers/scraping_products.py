"""Scraping Products serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from vsbuy_backend.products.models.scraping_products import ScrapingProduct
from vsbuy_backend.products.models.products import Product


class ScrapingProductModelSerializer(serializers.ModelSerializer):
    """Scraping Product model serializer."""

    class Meta:
        """Meta class."""
        model = ScrapingProduct
        fields = (
            'name',
            'price',
            'url',
            'picture',
            'store',
        )

        depth = 1

        read_only_fields = (
            'name',
            'price',
            'url',
            'picture',
            'store',
        )


class ScrapingProductNoUserSerializer(serializers.ModelSerializer):
    """Scraping Product No login user serializer."""

    class Meta:
        """Meta class."""
        model = ScrapingProduct
        fields = (
            'name',
            'price',
            'picture',
            'store',
        )

        depth = 1

        read_only_fields = (
            'name',
            'price',
            'picture',
            'store',
        )


class CreateScrapingProductSerializer(serializers.Serializer):

    """Save in the databases the products scrapped by the DS"""

    name = serializers.CharField(min_length=2, max_length=255)
    price = serializers.DecimalField(max_digits=19, decimal_places=10)
    url = serializers.URLField(min_length=3)
    picture = serializers.URLField(min_length=3, required=False)
    product = serializers.CharField()
    store = serializers.IntegerField(help_text='1 Amazon, 2 MercadoLibre, 3 Ebay')

    def validate_product(self, data):
        """Verify that the product keyword does not exist in the databases."""
        try:
            product = Product.objects.get(name=data)
        except Product.DoesNotExist:
            """Create a new keyword in the product parametric list"""
            product = Product.objects.create(name=data)

        return data

    def create(self, data):
        "Save the product scraped"
        scrap_product = ScrapingProduct.objects.create(
            name=data['name'],
            price=data['price'],
            url=data['url'],
            store_id=int(data['store']),
            product_id=Product.objects.get(name=data['product']).id
        )

        return scrap_product
