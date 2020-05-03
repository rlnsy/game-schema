from games.models.games_session import Session
from games.models.games_core import Game
from util.fn_request import (req_fields as fields_or_403, get_by_id)
from .players import auth_player
from rest_framework.views import Response
from util import http_status as status

def create_game_session(creator, game):
    s = Session(creator_agent_id=creator.agent_id, game_id=game)
    s.save()
    return Response({
        'message': "Session created"
    }, status=status.SUCCESS_CREATE)
    

def create_session(request):
    return fields_or_403(request, 
        ['game_id', 'creator_name', 'creator_token'], 
            lambda d: 
                auth_player(
                    d['creator_name'],
                    d['creator_token'],
            lambda p:
                get_by_id(Game, d['game_id'], 
            lambda g: 
                create_game_session(p, g))))
