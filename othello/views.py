from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Game
from .game_logic import init_board, get_result, is_valid_move, apply_move, get_next_player, is_game_over


@login_required
def index(request):
    games = Game.objects.filter(user=request.user, finished=False).order_by('-created_at')
    finished_games = Game.objects.filter(user=request.user, finished=True).order_by('-updated_at')

    context = {
        'games': games,
        'finished_games': finished_games,
    }

    return render(request, 'othello/index.html', context)


@login_required
def new(request):
    board = init_board()

    game = Game.objects.create(
        board=board,
        user=request.user,
    )

    return redirect('othello:play', game_id=game.id)


@login_required
def play(request, game_id):
    game = get_object_or_404(Game, id=game_id, user=request.user)

    if request.method == 'POST':
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))
        
        if is_valid_move(game.board, row, col, game.current_turn):
            apply_move(game.board, row, col, game.current_turn)

            next_turn = get_next_player(game.board, game.current_turn)
            if is_game_over(game.board) or next_turn is None:
                game.finished = True
                result = get_result(game.board)
                game.winner = result['winner']
            else:
                game.current_turn = next_turn
                
            game.save()

            return redirect('othello:play', game_id=game.id)

    result = get_result(game.board)
    black_count, white_count = result['black_count'], result['white_count']

    context = {
        'game': game,
        'black_count': black_count,
        'white_count': white_count,
    }

    return render(request, 'othello/play.html', context)