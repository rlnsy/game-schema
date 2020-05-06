from django.test import TestCase
from games.api.internal.games import list_games
from games.api.internal.games import list_roles
from games.api.internal.players import create_player
from games.api.internal.session import create_session
from games.api.internal.session import list_session_roles


class LogWrapperTests(TestCase):

    fixtures = ["dice"]

    def test_default_creator_roles(self):
        game_id = list_games()[0]['id']
        role_id = list_roles(game_id)[0]['id'] # there is only one role
        user_name = 'test1'
        display_name = "Test user 1"
        token = create_player(user_name, display_name)['player_token']
        session_id = create_session(game_id, user_name, token)['session_id']
        roles = list_session_roles(session_id, user_name, token)
        self.assertEqual(len(roles), 1)
        self.assertEqual(roles[0], {
            'user_name': user_name,
            'role_id': role_id,
            'active': True
        })

    """ TODO: add error cases """
