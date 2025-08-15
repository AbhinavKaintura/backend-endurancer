from django.db import models
from accounts.models import User

class JournalEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journal_entries')
    content = models.TextField()
    encrypted_content = models.TextField(blank=True, null=True)
    sentiment_score = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    detected_emotions = models.JSONField(blank=True, null=True)
    ai_prompt_used = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'journal_entries'
        ordering = ['-created_at']

    def __str__(self):
        return f"Entry by {self.user.email} - {self.created_at.strftime('%Y-%m-%d')}"

    @property
    def word_count(self):
        return len(self.content.split())

    @property
    def sentiment_label(self):
        if self.sentiment_score is None:
            return "Not analyzed"
        if self.sentiment_score >= 5:
            return "Very Positive"
        elif self.sentiment_score >= 2:
            return "Positive"
        elif self.sentiment_score >= -2:
            return "Neutral"
        elif self.sentiment_score >= -5:
            return "Negative"
        return "Very Negative"
