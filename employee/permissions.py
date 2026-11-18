from rest_framework.permissions import BasePermission
class IsOwner(BasePermission):
    def has_permission(self,request,view):
        if request.method=="GET":
            return request.user.is_authenticated

    def has_object_permission(self,request,view,obj):
        return obj.is_superuser==request.user