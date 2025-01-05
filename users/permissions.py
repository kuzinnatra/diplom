from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """Проверка, является ли пользователь Библиотекарем"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Librarian').exists()