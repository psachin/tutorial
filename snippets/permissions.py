from rest_framework import permissions


class IsOwneroReadOnly(permissions.BasePermission):
    '''
    Custom permissions to only allow owners of an object to edit it.
    '''
    def has_object_permission(self, request, view, obj):
        '''
        Read permissions are allowed to any request,
        Allow GET, HEAD and OPTIONS request
        '''
        if request.method in permissions.SAFE_METHODS:
            return True

        # rw access to owner of snippet
        return obj.owner == request.user
