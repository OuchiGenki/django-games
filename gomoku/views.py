from django.shortcuts import render
from .models import Game

def index(request):
    games = Game.objects.filter(user=request.user, finished=False).order_by('-created_at').first()
    context = {
        'games': games,
    }
    return render(request, 'gomoku/index.html', context)