from django.contrib import admin
from .models import SoundscapeContent, UserPlaylistActivity

@admin.register(SoundscapeContent)
class SoundscapeContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'subcategory', 'duration_minutes', 'created_at']
    list_filter = ['category', 'subcategory', 'created_at']
    search_fields = ['title']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Content Information', {
            'fields': ('title', 'category', 'subcategory', 'duration_minutes')
        }),
        ('Media', {
            'fields': ('audio_url',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

@admin.register(UserPlaylistActivity)
class UserPlaylistActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'listened_duration_minutes', 'completion_percentage', 'completed', 'created_at']
    list_filter = ['completed', 'created_at', 'content__category']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'content__title']
    readonly_fields = ['created_at', 'completion_percentage']
    
    fieldsets = (
        ('Activity Information', {
            'fields': ('user', 'content')
        }),
        ('Listening Data', {
            'fields': ('listened_duration_minutes', 'completion_percentage', 'completed')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'content')
