from games.models.games_session import HasRole, Session
from games.models.games_core import Game, Role
from games.models.games_players import Agent
from .logic_dispatch import find as find_logic
from .util.model_ops import get_by_id, remove_by_id, assert_nexist, assert_exist
from .players import auth_player
from rest_framework import serializers
from .exceptions import NotFound, NotAllowed
from games.logic.exceptions import LogicKeyError
from .util.game_wrapper import exec_logic

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    creator_agent_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    game_id = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    class Meta:
        model = Session
        fields = ['creator_agent_id', 'game_id', 'time_init']

def list_sessions():
    sessions = Session.objects.all()
    def transform(s):
        return {
            'started': s['time_init'],
            'creator_id': s['creator_agent_id'],
            'game_id': s['game_id']
        }
    return list([transform(SessionSerializer(s).data) for s in sessions])

def create_game_session(creator, game):
    def adopt_creator_roles(game_logic, session_id, k):
        def adopt_all(roles, k):
            for r in roles:
                try:
                    adopt_role(creator.agent_id, r, session_id)
                except NotFound:
                    raise LogicKeyError(r)
            return k()
        return exec_logic(
            game_logic.default_creator_roles,
            lambda r: adopt_all(r, k))
    s = Session(creator_agent_id=creator.agent_id, game_id=game)
    s.save()
    session_id = s.pk
    return find_logic(game.id,
        lambda l:
            adopt_creator_roles(l, session_id,
                lambda: {
                    'message': "Session created",
                    'session_id': session_id
                }))

def create_session(game_id, creator_name, creator_token):
    return auth_player(
                    creator_name,
                    creator_token,
                lambda p:
                    get_by_id(Game, game_id, 
                lambda g: 
                    create_game_session(p, g)))

def delete_session(session_id, creator_name, creator_token):
    return auth_player(creator_name, creator_token,
        lambda p:
            remove_by_id(Session, session_id,
                lambda: {
                    'message': "Session %d deleted" % session_id
                }))

class SessionRoleSerializer(serializers.HyperlinkedModelSerializer):
    session_id = serializers.PrimaryKeyRelatedField(read_only=True)
    agent_id = serializers.PrimaryKeyRelatedField(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = HasRole
        fields = ['session_id', 'agent_id', 'role_id', 'is_active']

def list_session_roles(session_id, player_name, player_token):
    if type(session_id) is not int:
        raise Exception("session_id must be an integer")
    serialize = SessionRoleSerializer
    def transform(record):
        return {
            'user_name': record['agent_id'],
            'role_id': record['role_id'],
            'active': record['is_active']
        }
    def get():
        return HasRole.objects.filter(session_id=session_id )
    def check_for_involvment(k):
        try:
            return assert_exist(
                HasRole.objects.filter(
                    session_id=session_id,
                    agent_id=player_name,
                ), lambda: k())
        except NotFound:
            raise NotAllowed(
        "Player %s is not involved in session %d" % (player_name, session_id))
    return auth_player(player_name, player_token,
        lambda p:
            check_for_involvment(
                lambda: list([transform(serialize(r).data) for r in get()])))

def adopt_role(agent_id, role_id, session_id):
    def create(agent, role, session):
        record = HasRole(
            session_id=session,
            agent_id=agent,
            role_id=role,
            is_active=True )
        record.save()
        return {
            'message': ""
        }
    return assert_nexist(
        HasRole.objects.filter(
            session_id=session_id,
            agent_id=agent_id,
            role_id=role_id,
            is_active=True ),
        lambda: get_by_id(Agent, agent_id,
        lambda a: get_by_id(Role, role_id,
        lambda r: get_by_id(Session, session_id,
        lambda s: create(a, r, s)))))
