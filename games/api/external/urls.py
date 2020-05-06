from django.urls import path

from .views import (
    GameListAPIView,
    PlayerAPIView,
    SessionAPIView,
    SessionRolesAPIView,
    ActionAPIView,
    ActionTypesAPIView
)


urlpatterns = [
    path('games', GameListAPIView.as_view(), name='game-list'),
    path('game/<game_id>/action-types', ActionTypesAPIView.as_view(), name='game-action-types'),
    path('player', PlayerAPIView.as_view(), name='player'),
    path('session', SessionAPIView.as_view(), name='session'),
    path('session/<int:session_id>/roles', SessionRolesAPIView.as_view(), name='session-roles'),
    path('action', ActionAPIView.as_view(), name='action')
]
