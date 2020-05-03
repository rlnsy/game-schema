from games.models.games_session import Session
from games.models.games_core import Game
from util.fn_request import (req_fields as fields_or_403, get_by_id)
from rest_framework.views import Response
from util import http_status as status

def create_game_session(game):
    s = Session(game_id=game)
    s.save()
    return Response({
        'message': "Session created"
    }, status=status.SUCCESS_CREATE)

def create_session(request):
    return fields_or_403(request, 
        ['game_id'], 
            lambda d: get_by_id(Game, d['game_id'], create_game_session))
