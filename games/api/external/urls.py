from django.urls import path

from .views import (
    GameListAPIView,
    PlayerAPIView,
    SessionAPIView
)


urlpatterns = [
    path('games', GameListAPIView.as_view(), name='game-list'),
    path('player', PlayerAPIView.as_view(), name='player'),
    path('session', SessionAPIView.as_view(), name='session')
]
