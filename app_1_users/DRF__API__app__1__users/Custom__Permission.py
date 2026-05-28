from rest_framework.permissions import BasePermission, SAFE_METHODS

# Custom Permission
class custom__permission__function(BasePermission):
    """
    Allow only superuser (is_superuser=True) to POST, PUT, PATCH, DELETE.
    Others can only GET.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_superuser  # Only admin allowed for unsafe methods
