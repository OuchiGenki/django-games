from django.shortcuts import render
from .models import Game, Guess
from .forms import GuessForm
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg, Prefetch


def create_answer():
    return ''.join([str(randint(0, 9)) for _ in range(4)])


@login_required
def play(request):
    game = request.user.game_set.filter(is_finished=False).first()
    if game is None:
        game = Game.objects.create(answer=create_answer(), user=request.user)

    guess = None
    if request.method == 'POST':
        form = GuessForm(request.POST)
        if form.is_valid():
            game.attempts += 1

            guess = Guess()
            guess.number = form.cleaned_data['number']
            guess.game = game
            guess.attempts = game.attempts

            guess.set_hit_blow()

            guess.save()

            if guess.hit == 4:
                game.is_finished = True
            
            game.save()

    else:
        form = GuessForm()

    guesses = game.guess_set.all()

    context = {
        'game': game,
        'form': form,
        'guesses': guesses,
    }

    return render(request, 'HitAndBlow/game.html', context)


@login_required
def ranking(request):
    users = User.objects.prefetch_related(
        Prefetch('game_set', Game.objects.filter(is_finished=True))
    )
    rankings = []

    for user in users:
        games = user.game_set.all()
        num_game = len(games)

        if num_game == 0:
            continue

        avg_attempts = games.aggregate(Avg('attempts'))['attempts__avg']

        rankings.append(
            {
                'user': user,
                'avg_attempts': avg_attempts,
            }
        )
    
    rankings.sort(key=lambda x: x['avg_attempts'])

    context = {'rankings': rankings}

    return render(request, 'HitAndBlow/ranking.html', context)
