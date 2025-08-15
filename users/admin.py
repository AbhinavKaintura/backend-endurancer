from django.contrib import admin
from .models import UserProfile, UserProgress

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'stress_level', 'age_group', 'created_at']
    list_filter = ['stress_level', 'age_group', 'created_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(UserProgress)
class UserProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'current_level', 'level_name', 'endurance_points', 'daily_streak', 'total_sessions']
    list_filter = ['level_name', 'current_level', 'updated_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'updated_at']
