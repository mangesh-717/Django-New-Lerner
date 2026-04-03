from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, PostPermission


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


@admin.register(PostPermission)
class PostPermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'can_read', 'can_write')
    list_filter = ('can_read', 'can_write')