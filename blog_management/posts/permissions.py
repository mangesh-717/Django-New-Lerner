# blog/permissions.py

from rest_framework.permissions import BasePermission
from posts.models import Post

class CanAssignPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Allow admin always
        if request.user.role == 'admin':
            return True

        # For POST (creating permission)
        if request.method == 'POST':
            post_id = request.data.get('post')

            if not post_id:
                return False

            try:
                post = Post.objects.get(id=post_id)
            except Post.DoesNotExist:
                return False

            # Allow only if user is author of post
            return post.author == request.user

        return True