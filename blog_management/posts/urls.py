from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, PostPermissionViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('permissions', PostPermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]