from games import index
from rest_framework.views import Response
from .exceptions import NotFound

def find(game_id, k):

    if game_id == 'Dice':
        return k(index.dice_logic)
    else:
        raise NotFound("Could not load logic for game '%s'" % game_id)