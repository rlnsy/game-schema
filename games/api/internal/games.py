from games.models import Game
from rest_framework import serializers

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id']

def list_games():
    games = Game.objects.all()
    return list([GameSerializer(g).data for g in games])
    