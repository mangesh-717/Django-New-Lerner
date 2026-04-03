from rest_framework import serializers
from .models import Post, PostPermission


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class PostPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPermission
        fields = '__all__'