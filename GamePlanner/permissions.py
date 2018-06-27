from rest_framework import permissions

class IsInProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        is_authorized = obj.owner == request.user

        if request.method in permissions.SAFE_METHODS:
            return True

        project_user_data = request.user.project_users_data.filter(project==obj).first()
        if project_user_data:
            is_authorized = project_user_data.is_active

        return is_authorized