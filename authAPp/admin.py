from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import RevokedToken

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class RevokedTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'is_explicit')  # Assuming 'created_at' is a DateTimeField
    search_fields = ('token',)
    list_filter = ('is_explicit',)  # Add any other fields you want to filter by

admin.site.register(RevokedToken, RevokedTokenAdmin)
