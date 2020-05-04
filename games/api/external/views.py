from rest_framework import generics, serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from games.models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id']

class GameListAPIView(generics.ListAPIView):
    queryset = Game.objects.all()   
    serializer_class = GameSerializer  # show all details
    permission_classes = [AllowAny]

from .util.fn_response import wrap_http_response
from .util.fn_request import req_fields

from games.api.internal.players import create_player
class PlayerAPIView(APIView):
    def post(self, request):
        return req_fields(request, ['user_name', 'display_name'],
            lambda d:
            wrap_http_response(
                lambda: create_player(d['user_name'], d['player_name']),
                success_create=True))

from games.api.internal.session import create_session
class SessionAPIView(APIView):
    def post(self, request):
        return req_fields(request,
            ['game_id', 'creator_name', 'creator_token'],
            lambda d:
            wrap_http_response(
                lambda: create_session(
                    d['game_id'],
                    d['creator_name'],
                    d['creator_token']
                ), success_create=True))
