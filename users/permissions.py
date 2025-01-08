from rest_framework.permissions import BasePermission

class IsLibrarian(BasePermission):
    """Проверка, является ли пользователь Библиотекарем"""
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Librarian').exists()



class IsOwner(BasePermission):
    """Проверяет является ли пользователь владельцем"""
    def has_object_permission(self, request, view, obj):
        if obj.id == request.user.id:
            return True
        return False