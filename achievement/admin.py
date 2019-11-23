from django.contrib import admin

# Register your models here.
from achievement.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('slug', 'points')
    fields = ('slug', 'points', 'description', 'image')
