from games.models.games_players import Agent, Player, PLAYER_TOKEN_LENGTH, PLAYER_TOKEN_CHARS
from util.fn_request import (req_fields as fields_or_403, assert_nexist)
from rest_framework.views import Response
import random

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
        return Response({
            'message': "Player created",
            'player_token': token
        }, status=201)
    return fn


def create_player(request):
    return fields_or_403(request, 
        ['user_name', 'display_name'], 
            lambda d: 
                create_agent(d['user_name'], 
                create_player_from_agent(d['display_name'])))
