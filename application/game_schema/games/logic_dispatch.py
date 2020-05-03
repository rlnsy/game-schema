from . import index
from rest_framework.views import Response
from util import http_status as status

def find(game_id, k):

    if game_id == 'Dice':
        return k(index.dice_logic)
    else:
        return Response("Could not load logic for game '%s'" % game_id, status=status.SERVER_INTERNAL_ERROR)
