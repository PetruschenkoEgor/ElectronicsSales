from rest_framework import permissions


class IsActiveUser(permissions.BasePermission):
    """Если пользователь активный."""

    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
