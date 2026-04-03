from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role',)
    search_fields = ('username',)