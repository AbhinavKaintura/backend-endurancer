from django.db import models
from accounts.models import User

class SoundscapeContent(models.Model):
    CATEGORY_CHOICES = [
        ('focus', 'Focus'),
        ('relaxation', 'Relaxation'),
        ('sleep', 'Sleep'),
    ]
    
    SUBCATEGORY_CHOICES = [
        ('binaural_beats', 'Binaural Beats'),
        ('nature_sounds', 'Nature Sounds'),
        ('classical', 'Classical'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=50, choices=SUBCATEGORY_CHOICES)
    audio_url = models.URLField(max_length=500)
    duration_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'soundscape_content'
        ordering = ['title']

    def __str__(self):
        return f"{self.title} ({self.category}/{self.subcategory})"

class UserPlaylistActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlist_activities')
    content = models.ForeignKey(SoundscapeContent, on_delete=models.CASCADE)
    listened_duration_minutes = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_playlist_activity'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.content.title} - {'Completed' if self.completed else 'Partial'}"

    @property
    def completion_percentage(self):
        if self.listened_duration_minutes and self.content.duration_minutes:
            return min(100, (self.listened_duration_minutes / self.content.duration_minutes) * 100)
        return 0
