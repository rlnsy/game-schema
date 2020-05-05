from games.models.games_session import HasRole, Session
from games.models.games_core import Game
from .logic_dispatch import find as find_logic
from .util.model_ops import get_by_id
from .players import auth_player

def create_game_session(creator, game):
    def create(game_logic):
        s = Session(creator_agent_id=creator.agent_id, game_id=game)
        s.save()
        game_logic.on_session_create(creator.agent_id)
        return {
            'message': "Session created",
            'session_id': s.pk
        }
    return find_logic(game.id, create)

def create_session(game_id, creator_name, creator_token):
    return auth_player(
                    creator_name,
                    creator_token,
                lambda p:
                    get_by_id(Game, game_id, 
                lambda g: 
                    create_game_session(p, g)))

#def delete_session(session_id, )

# def adopt_role(agent, role, session):
#     def create():
#         record = HasRole(
#             session_id=session,
#             agent_id=agent,
#             role_id=role,
#             is_active=True )
#         record.save()
#     # return 
