from games.models.games_players import Agent, Player, PLAYER_TOKEN_LENGTH, PLAYER_TOKEN_CHARS
import random
from .exceptions import NotAllowed
from .util.model_ops import assert_nexist, get_by_id, remove_by_id
from rest_framework import serializers


def create_agent(name, k):
    def create():
        a = Agent(id=name)
        a.save()
        return a
    return assert_nexist(
        Agent.objects.filter(id=name),
        lambda: k(create()))

def create_player_from_agent(display_name):
    def fn(a):
        token = ''.join([random.choice(PLAYER_TOKEN_CHARS) for i in range(PLAYER_TOKEN_LENGTH)])
        p = Player(agent_id=a, display_name=display_name, token=token)
        p.save()
        return {
            'message': "Player created",
            'player_token': token
        }
    return fn

def create_player(user_name, display_name):
    return create_agent(user_name,
                create_player_from_agent(display_name))

def auth_player(name, token, k):
    def check_token(p, k):
        if p.token == token:
            return k(p)
        else:
            raise NotAllowed("Bad token for player '%s'" % name)
    return get_by_id(Player, name,
        lambda p: check_token(p, k))

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    agent_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    class Meta:
        model = Player
        fields = ['agent_id', 'display_name']

def list_players():
    players = Player.objects.all()
    def transform(p):
        return {
            'user_name': p['agent_id'],
            'display_name': p['display_name']
        }
    return list([transform(PlayerSerializer(p).data) for p in players])


def delete_player(name, token):
    return remove_by_id(Player, name,
        lambda: {
            'message': "Player '%s' deleted" % name
        })
