"""Products permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from vsbuy_backend.users.models import User


class IsSuperUser(BasePermission):
    """Allow create objects only to the superusers user."""


    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        try:
            User.objects.get(
                user=request.user,
                is_superuser=True,
            )
        except User.DoesNotExist:
            return False
        return True