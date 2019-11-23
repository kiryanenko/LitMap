from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User
from places.admin import place_action


@admin.register(User)
class PersonAdmin(UserAdmin):
    list_display = ('username', 'email', 'rating')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('date_joined',)

    def place_push(self, request, queryset):
        return place_action(self, request, queryset)
    place_push.short_description = 'Push уведомление о месте'

    actions = [place_push]
