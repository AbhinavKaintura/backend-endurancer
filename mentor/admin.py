from django.contrib import admin
from .models import MentorConversation

@admin.register(MentorConversation)
class MentorConversationAdmin(admin.ModelAdmin):
    list_display = ['user', 'message_type', 'session_id', 'created_at']
    list_filter = ['message_type', 'created_at']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'content']
    readonly_fields = ['created_at', 'session_id']
    
    fieldsets = (
        ('Conversation Information', {
            'fields': ('user', 'session_id', 'message_type')
        }),
        ('Message Content', {
            'fields': ('content', 'context_data')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
