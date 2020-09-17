from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # print(request.user)
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj)
        return obj.user == request.user
