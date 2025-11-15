from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    PLAYER_CHOICES = [
        ('B', 'Black'),
        ('W', 'White'),
    ]

    board = models.JSONField(default=list)
    current_turn = models.CharField(max_length=1, default='B', choices=PLAYER_CHOICES)
    is_finished = models.BooleanField(default=False)
    winner = models.CharField(max_length=1, choices=PLAYER_CHOICES, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gomoku_games')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Game {self.id} by {self.user.username}"