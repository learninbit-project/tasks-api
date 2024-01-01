from rest_framework import permissions


class TaskPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # only the owner of the object can read
            return obj.created_by == request.user

        if view.action in ["update", "partial_update"]:
            # only the owner of the object can update
            return obj.created_by == request.user

        if view.action == "destroy":
            # only the owner of the object can delete
            return obj.created_by == request.user

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True


class TaskCategoryPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # only the owner of the object can read
            return obj.created_by == request.user

        if view.action in ["update", "partial_update"]:
            # only the owner of the object can update
            return obj.created_by == request.user

        if view.action == "destroy":
            # only the owner of the object can delete
            return obj.created_by == request.user

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # any authenticated user can list objects
            return request.user.is_authenticated

        if view.action == "create":
            # any authenticated user can create
            return request.user.is_authenticated

        return True
