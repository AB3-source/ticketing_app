from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Allow full access only to admin users."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsSupport(permissions.BasePermission):
    """Allow access to support users (limited to assigned tickets)."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'support'


class IsTicketOwnerOrReadOnly(permissions.BasePermission):
    """Allow users to access their own tickets or admins."""
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.user.role == 'support':
            return obj.assigned_to == request.user or request.method in permissions.SAFE_METHODS
        return obj.created_by == request.user or request.method in permissions.SAFE_METHODS


class TicketAccessPermission(permissions.BasePermission):
    """
    Controls ticket actions:
    - Users: can create/view their own
    - Support: can view/update assigned
    - Admin: full access
    """
    def has_permission(self, request, view):
        # Authenticated users only
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Admins: full control
        if user.role == 'admin':
            return True

        # Support: can view & update assigned tickets
        if user.role == 'support':
            if obj.assigned_to == user:
                return True
            return request.method in permissions.SAFE_METHODS

        # Regular users: can view or create their own
        if user.role == 'user':
            if request.method in ['GET', 'HEAD', 'OPTIONS']:
                return obj.created_by == user
            if request.method == 'POST':
                return True
            return False

        return False
