from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Post, PostPermission
from .serializers import PostSerializer, PostPermissionSerializer
from .permissions import CanAssignPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, CanAssignPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# blog/views.py

from rest_framework.viewsets import ModelViewSet
from .permissions import CanAssignPermission

class PostPermissionViewSet(ModelViewSet):
    queryset = PostPermission.objects.all()
    serializer_class = PostPermissionSerializer
    permission_classes = [CanAssignPermission]   # 👈 ADD THIS


