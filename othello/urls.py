from django.urls import path
from . import views

app_name = 'othello'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('play/<int:game_id>/', views.play, name='play'),
]