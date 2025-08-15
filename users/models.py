from django.db import models
from accounts.models import User

class UserProfile(models.Model):
    STRESS_LEVEL_CHOICES = [
        ('several_times_daily', 'Several times daily'),
        ('daily', 'Daily'),
        ('few_times_week', 'Few times a week'),
        ('rarely', 'Rarely'),
    ]
    
    AGE_GROUP_CHOICES = [
        ('child', 'Child'),
        ('teen', 'Teen'),
        ('adult', 'Adult'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    goals = models.JSONField(default=list, help_text="Array of user goals")
    stress_level = models.CharField(max_length=50, choices=STRESS_LEVEL_CHOICES, blank=True, null=True)
    aspirational_goals = models.JSONField(default=list, help_text="Desired states")
    age_group = models.CharField(max_length=20, choices=AGE_GROUP_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_profiles'

    def __str__(self):
        return f"{self.user.email} - Profile"

class UserProgress(models.Model):
    KOSHA_LEVELS = [
        ('Annamaya', 'Annamaya - Physical'),
        ('Pranamaya', 'Pranamaya - Energy'),
        ('Manomaya', 'Manomaya - Mental'),
        ('Vijnanamaya', 'Vijnanamaya - Wisdom'),
        ('Anandamaya', 'Anandamaya - Bliss'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    endurance_points = models.IntegerField(default=0)
    current_level = models.IntegerField(default=1)
    level_name = models.CharField(max_length=50, choices=KOSHA_LEVELS, default='Annamaya')
    daily_streak = models.IntegerField(default=0)
    total_sessions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_progress'

    def __str__(self):
        return f"{self.user.email} - Level {self.current_level} ({self.level_name})"
