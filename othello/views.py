from django.shortcuts import render


def index(request):
    return render(request, 'othello/index.html')


def new(request):
    return render(request, 'othello/new.html')


def play(request):
    return render(request, 'othello/play.html')