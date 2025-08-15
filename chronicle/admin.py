from django.contrib import admin
from .models import JournalEntry

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'sentiment_label', 'sentiment_score', 'word_count', 'created_at']
    list_filter = ['created_at', 'sentiment_score']
    search_fields = ['user__email', 'user__first_name', 'user__last_name', 'content']
    readonly_fields = ['created_at', 'updated_at', 'word_count', 'sentiment_label']
    
    fieldsets = (
        ('Entry Information', {
            'fields': ('user', 'content', 'ai_prompt_used')
        }),
        ('AI Analysis', {
            'fields': ('sentiment_score', 'sentiment_label', 'detected_emotions')
        }),
        ('Security', {
            'fields': ('encrypted_content',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
