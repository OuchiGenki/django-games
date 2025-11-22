from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gomoku.urls')),
    path('accounts/', include('accounts.urls')),
    path('hitandblow/', include('HitAndBlow.urls')),
    path('othello/', include('othello.urls')),
    path('gomoku/', include('gomoku.urls')),
]
