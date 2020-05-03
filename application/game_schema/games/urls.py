from django.urls import path

from .views import (
    GameListAPIView,
    PlayerAPIView
)


urlpatterns = [
    path('games', GameListAPIView.as_view(), name='game-list'),
    path('player', PlayerAPIView.as_view(), name='game-list')
]
