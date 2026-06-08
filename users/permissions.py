from django.core.exceptions import PermissionDenied
from .models import RolePermission, UserRole

def has_resource_permission(user, resource_name, action_name):
    if not user.is_authenticated or not user.is_active:
        return False
    user_roles = UserRole.objects.filter(user=user).values_list('role_id', flat=True)
    return RolePermission.objects.filter(
        role_id__in=user_roles,
        resource__name=resource_name,
        action__name=action_name,
        allowed=True
    ).exists()

# DRF Permission class (recommended)
from rest_framework.permissions import BasePermission

class CustomRBACPermission(BasePermission):
    resource = None  # Set in view
    action = None

    def has_permission(self, request, view):
        if not request.user or not request.user.is_active:
            return False  # 401 handled by auth
        return has_resource_permission(request.user, self.resource or view.resource, self.action or request.method.lower())

def mock_projects(request):
    if not has_resource_permission(request.user, 'projects', 'list'):
        raise PermissionDenied  # 403
    return render(request, 'mock.html', {'data': ['Project1', 'Project2']})