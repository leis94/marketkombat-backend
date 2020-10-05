"""User tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

# Model
from vsbuy_backend.users.models import User


class UserManagerTestCase(TestCase):
    """Users manage test case."""

    def setUp(self):
        """Test case setup."""
        # Crear un usuario en BD.
        self.user = User.objects.create(
            first_name='Daniel',
            last_name='Silva',
            email='test@gmail.com',
            username='leistest94',
            password='admin123#',
            is_verified=True,
        )


    def test_user_create(self):
        """Create a user and valide that was created."""
        user = User.objects.get(username=self.user.username)
        self.assertIsNotNone(user.username)


    def test_user_signup(self):
        """Create a user using the API endpoint."""
        url = '/users/signup/'
        data = {"email": "test2@gmail.com",
                "username": "test",
                "password": "admin123#",
                "password_confirmation": "admin123#",
                "first_name": "test",
                "last_name": "test",
                "phone_number": "987654321"
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_user_login(self):
        """Valide the user login."""
        self.test_user_signup()
        url = '/users/login/'
        data = {"email": "test2@gmail.com",
                "password": "admin123#",
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
