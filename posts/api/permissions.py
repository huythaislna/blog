from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS

class IsUpdated(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        if not obj:
            return super().has_permission(request, view)
        else:
            if request.method in SAFE_METHODS:
                return True
        return request.user == obj.author
