from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Game
from .game_logic import init_board, is_valid_move, apply_move, is_game_over
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    games = Game.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'games': games,
    }
    return render(request, 'gomoku/index.html', context)


@login_required
def new(request):
    board = init_board()
    game = Game.objects.create(
        board=board,
        user=request.user,
    )
    return redirect('gomoku:play', game_id=game.id)


@login_required
def play(request, game_id):
    game = get_object_or_404(Game, id=game_id, user=request.user)
    context = {
        'game': game,
        'board': game.board,
        'current_turn': game.current_turn,
    }
    return render(request, 'gomoku/play.html', context)


def api_move(request):
    row, col = int(request.GET.get('row')), int(request.GET.get('col'))
    game_id = request.GET.get('game_id')

    game = get_object_or_404(Game, id=game_id, user=request.user)
    board = game.board
    color = game.current_turn

    moved = False

    # 有効手なら適用して状態を更新
    if is_valid_move(board, row, col, color):
        moved = True
        new_board = apply_move(board, row, col, color)
        game.board = new_board
        game.current_turn = 'W' if color == 'B' else 'B'

        # ゲーム終了判定（移動が行われた場合のみ）
        game_over = is_game_over(new_board)
        if not game.is_finished and game_over and game_over['flag']:
            game.is_finished = True
            game.winner = game_over['winner']

        game.save()

    return JsonResponse({
        'board': game.board,
        'is_finished': game.is_finished,
        'current_turn': game.current_turn,
        'moved': moved,
        'winner': game.winner,
    })