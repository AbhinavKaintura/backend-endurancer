from django.contrib import admin
from .models import GameSession

@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'game_type', 'difficulty_level', 'score', 'won', 'points_earned', 'performance_rating', 'created_at']
    list_filter = ['game_type', 'difficulty_level', 'won', 'created_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name']
    readonly_fields = ['created_at', 'performance_rating']
    
    fieldsets = (
        ('Game Information', {
            'fields': ('user', 'game_type', 'difficulty_level')
        }),
        ('Game Results', {
            'fields': ('score', 'won', 'duration_minutes', 'moves_count', 'points_earned', 'performance_rating')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
