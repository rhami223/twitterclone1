from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreateForm
from .models import TwitterUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = TwitterUser
    list_display = ['username', 'email', ]
    fieldsets = UserAdmin.fieldsets + (
        ('additional info', {'fields': ('followed', )}),
    )
admin.site.register(TwitterUser, CustomUserAdmin)