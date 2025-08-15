from django.contrib import admin
from .models import SanctuaryContent, UserActivity

@admin.register(SanctuaryContent)
class SanctuaryContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'content_type', 'difficulty_level', 'duration_minutes', 'endurance_points', 'created_at']
    list_filter = ['content_type', 'difficulty_level', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Content Information', {
            'fields': ('title', 'description', 'content_type', 'difficulty_level', 'duration_minutes')
        }),
        ('Media URLs', {
            'fields': ('audio_url', 'video_url', 'thumbnail_url')
        }),
        ('Categorization', {
            'fields': ('age_groups', 'tags', 'endurance_points')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'activity_type', 'duration_minutes', 'points_earned', 'completed_at']
    list_filter = ['activity_type', 'completed_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['completed_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
