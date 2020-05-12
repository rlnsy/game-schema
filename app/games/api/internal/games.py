from games.models import Game, Role
from rest_framework import serializers
from .util.model_ops import get_by_id

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['id']

def list_games():
    games = Game.objects.all()
    return list([GameSerializer(g).data for g in games])

class RoleSerializer(serializers.HyperlinkedModelSerializer):
    game_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Role
        fields = ['id', 'game_id']

def list_roles(game_id):
    def transform(role):
        return { 'id': role['id'] }
    def list_all(game_id):
        roles = Role.objects.filter(game_id=game_id)
        return list([transform(RoleSerializer(r).data) for r in roles])
    return get_by_id(Game, game_id,
        lambda g: list_all(g.id))
    