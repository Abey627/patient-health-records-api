from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    """Allows access only to users with role 'doctor'."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'doctor'
        )

class IsPatient(BasePermission):
    """Allows access only to users with role 'patient'."""
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'profile') and
            request.user.profile.role == 'patient'
        )
