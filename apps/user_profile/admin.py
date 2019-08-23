from django.contrib import admin

from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

from apps.user_profile.models import UserModel


class UserModelAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name', 'email', 'date_birth')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(UserModel, UserModelAdmin)
