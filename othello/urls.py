from django.urls import path
from . import views

app_name = 'othello'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('play/', views.play, name='play'),
]