from django.db import models
from accounts.models import User

class SanctuaryContent(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('meditation', 'Meditation'),
        ('yoga', 'Yoga'),
        ('pranayama', 'Pranayama'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    content_type = models.CharField(max_length=50, choices=CONTENT_TYPE_CHOICES)
    duration_minutes = models.IntegerField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    age_groups = models.JSONField(default=list, help_text="Target age groups")
    audio_url = models.URLField(max_length=500, blank=True, null=True)
    video_url = models.URLField(max_length=500, blank=True, null=True)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)
    tags = models.JSONField(default=list, help_text="Content tags")
    endurance_points = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sanctuary_content'
        ordering = ['title']

    def __str__(self):
        return f"{self.title} ({self.content_type})"

class UserActivity(models.Model):
    ACTIVITY_TYPE_CHOICES = [
        ('meditation', 'Meditation'),
        ('journal', 'Journal'),
        ('game', 'Game'),
        ('mentor_chat', 'Mentor Chat'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_TYPE_CHOICES)
    content_id = models.IntegerField(blank=True, null=True)
    duration_minutes = models.IntegerField(blank=True, null=True)
    points_earned = models.IntegerField(blank=True, null=True)
    completed_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(blank=True, null=True, help_text="Additional activity data")

    class Meta:
        db_table = 'user_activities'
        ordering = ['-completed_at']

    def __str__(self):
        return f"{self.user.email} - {self.activity_type} - {self.completed_at.strftime('%Y-%m-%d')}"
