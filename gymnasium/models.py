from django.db import models
from accounts.models import User

class GameSession(models.Model):
    GAME_TYPE_CHOICES = [
        ('chaturanga', 'Chaturanga'),
        ('pachisi', 'Pachisi'),
        ('pallanguzhi', 'Pallanguzhi'),
    ]
    
    DIFFICULTY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_sessions')
    game_type = models.CharField(max_length=50, choices=GAME_TYPE_CHOICES)
    score = models.IntegerField(blank=True, null=True)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    duration_minutes = models.IntegerField(blank=True, null=True)
    moves_count = models.IntegerField(blank=True, null=True)
    won = models.BooleanField(blank=True, null=True)
    points_earned = models.IntegerField(default=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'game_sessions'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.game_type} - {'Won' if self.won else 'Lost'}"

    @property
    def performance_rating(self):
        if self.won:
            return "Excellent" if self.score > 80 else "Good"
        return "Keep practicing"
