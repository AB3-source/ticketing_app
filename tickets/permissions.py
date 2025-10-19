from rest_framework import permissions

class IsOwnerOrAssigneeOrStaff(permissions.BasePermission):
    """
    Object-level permission to allow editing only to:
      - ticket owner (created_by),
      - assigned user (assigned_to),
      - or staff users.
    Read allowed for authenticated users.
    """

    def has_permission(self, request, view):
        # Ensure user is authenticated for any access
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS are allowed for any authenticated user
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if user.is_staff:
            return True

        # owner or assignee may edit/delete
        if hasattr(obj, 'created_by') and obj.created_by == user:
            return True
        if hasattr(obj, 'assigned_to') and obj.assigned_to == user:
            return True

        return False
