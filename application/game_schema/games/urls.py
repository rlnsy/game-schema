from django.urls import path


from rest_framework import generics, serializers
from rest_framework.views import APIView, Response
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


from .players import create_player
class PlayerAPIView(APIView):
    def post(self, request):
        return create_player(request)


urlpatterns = [
    path('games', GameListAPIView.as_view(), name='game-list'),
    path('player', PlayerAPIView.as_view(), name='game-list')
]
