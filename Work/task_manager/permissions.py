from rest_framework import permissions

class IsCustomer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.customer

class IsEmployee(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.employee

class IsTaskOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            request.user == obj.customer.user or
            request.user == obj.employee.user or
            request.user.employee.is_superuser
        )

class IsEmployeeOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.employee or
            request.user.employee.is_superuser
        )
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user