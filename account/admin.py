from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import DrCUserChangeForm, DrSUserCreationsForm


# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ['national_code']
    add_form = DrSUserCreationsForm
    form = DrCUserChangeForm
    model = User
    list_display = (
        'national_code', 'phone_number', 'last_name', 'first_name', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('national_code', 'password')}),
        ('Personal info', {'fields': ('user_type', 'first_name', 'last_name','phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('dates', {'fields': ('date_joined',)}),
    )

    add_fieldsets = (
        (None, {'fields': ('national_code', 'password1', 'password2')}),
        ('Personal info', {'fields': ('user_type', 'first_name', 'last_name','phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('dates', {'fields': ('date_joined',)}),
    )


@admin.register(DrUser)
class DrUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization')


@admin.register(SickUser)
class SickUserAdmin(admin.ModelAdmin):
    list_display = ('user',)
