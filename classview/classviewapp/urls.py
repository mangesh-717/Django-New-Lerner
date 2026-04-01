

from django.urls import path
from .views import CustomPostListView, CustomPostDetailView

urlpatterns = [
    path('posts/', CustomPostListView.as_view(), name='custom-post-list'),
    path('posts2/', CustomPostDetailView.as_view(), name='custom-post-detail'),
]
