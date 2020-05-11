from django.urls import path, re_path

from .views import (
    GameListAPIView,
    PlayerAPIView,
    SessionAPIView,
    SessionRolesAPIView,
    ActionAPIView,
    ActionTypesAPIView
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Games Schema API",
      default_version='v1',
      description="Front-end for manipulating the system",
      terms_of_service="https://github.com/rlnsy/games-schema/blob/master/README.md",
      contact=openapi.Contact(email="dev.gmbx@yahoo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path('^swagger(?P<format>\\.json|\\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('games', GameListAPIView.as_view(), name='game-list'),
    path('game/<game_id>/action-types', ActionTypesAPIView.as_view(), name='game-action-types'),
    path('player', PlayerAPIView.as_view(), name='player'),
    path('session', SessionAPIView.as_view(), name='session'),
    path('session/<int:session_id>/roles', SessionRolesAPIView.as_view(), name='session-roles'),
    path('action', ActionAPIView.as_view(), name='action')
]
