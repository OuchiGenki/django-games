from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    answer = models.CharField(max_length=4)
    attempts = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Guess(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    attempts = models.IntegerField()
    number = models.CharField(max_length=4)
    hit = models.IntegerField()
    blow = models.IntegerField()

    def set_hit_blow(self):
        self.hit = sum([1 for g, a in zip(self.number, self.game.answer) if g == a])
        self.blow = sum([1 for g in self.number if g in self.game.answer]) - self.hit