"""Кастом пермишен."""
from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """Проверка на входе."""
    def has_permission(self, request, view):
        """Автор или только смотреть, или создать."""
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )

    def has_object_permission(self, request, view, obj):
        """Проверяем совпадает ли автор поста с пользователем из запроса,
        если да, то даем все права."""
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                )
