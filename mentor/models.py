import uuid
from django.db import models
from accounts.models import User

class MentorConversation(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentor_conversations')
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES)
    content = models.TextField()
    context_data = models.JSONField(blank=True, null=True, help_text="Related data like journal entries")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'mentor_conversations'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.user.email} - {self.message_type} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
