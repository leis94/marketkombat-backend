"""Products tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Model
from vsbuy_backend.products.models.products import Product
from vsbuy_backend.products.models.stores import Store
from vsbuy_backend.products.models.scraping_products import ScrapingProduct


class ProductManagerTestCase(TestCase):
    """Products manage test case."""

    def setUp(self):
        """Test case setup."""

        self.store = Store.objects.create(
            name='Amazon',
            logo='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1280px-Amazon_logo.svg.png',
        )

        self.product = Product.objects.create(
            name='Test',
        )

        self.scraping_product = ScrapingProduct.objects.create(
            name='Producto de prueba',
            picture='https://imagetest.com',
            url='https://test.com',
            price=544.45,
            product = self.product,
            store = self.store,
        )


    def test_store_create(self):
        store = Store.objects.get(name=self.store.name)
        self.assertIsNotNone(store.name)


    def test_product_create(self):
        product = Product.objects.get(name=self.product.name)
        self.assertIsNotNone(product.name)


    def test_scrap_create(self):
        """Create a scrap product and valide that was created."""
        scraping_product = ScrapingProduct.objects.get(name=self.scraping_product.name)
        self.assertIsNotNone(scraping_product.name)


    def test_scrap_search(self):
        """Verify request succed."""
        url = '/scrap/?search={}/'.format(
            self.product.name
        )
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)


    def test_list_favorites(self):
        """Verify request succed."""
        url = '/scrap/list/favorites/'
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
