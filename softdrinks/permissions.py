from rest_framework import permissions

class IsStaffEditorPermissions(permissions.DjangoModelPermissions):
    def has_permission(self,request,view):
        user=request.user
        if not user.is_staff:
            return False
        return super.has_permission(request,view)

    