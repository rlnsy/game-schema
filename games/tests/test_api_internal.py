from django.test import TestCase
from games.api.internal.exceptions import NotAllowed, NotFound

from games.api.internal.games import list_games
class GameResourceEmptyTests(TestCase):

    def test_list_empty(self):
        games = list_games()
        self.assertEqual(games, [])


class GameResourceTests(TestCase):

    fixtures = ["dice"] # intstall the demo game for these tests

    def test_list_empty(self):
        games = list_games()
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0], {'id': 'Dice'})


from games.api.internal.games import list_roles
class RoleResourceTests(TestCase):

    fixtures = ["dice"]
    
    def test_list_roles_bad_game(self):
        try:
            roles = list_roles('Mario')
            self.fail()
        except NotFound:
            pass

    def test_list_roles(self):
        roles = list_roles('Dice')
        self.assertEqual(len(roles), 1)
        self.assertEqual(roles[0], { 'id': 'Dice_roller'})


from games.api.internal.players import list_players, create_player, delete_player
class PlayerResourceTests(TestCase):

    def test_players_empty(self):
        players = list_players()
        self.assertEqual(players, [])

    def test_add_delete_player(self):
        self.assertEqual(list_players(), [])
        # create
        user_name = 'test1'
        display_name = "Test user 1"
        result = create_player(user_name, display_name)
        self.assertIsInstance(result, dict)
        self.assertEqual(len(result.keys()), 2)
        self.assertIn('message', result)
        self.assertIn('player_token', result)
        token = result['player_token'] 
        # get
        players = list_players()
        self.assertEqual(len(players), 1)
        player = players[0]
        self.assertEqual(len(player.keys()), 2)
        self.assertEqual(player['user_name'], user_name)
        self.assertEqual(player['display_name'], display_name)
        # delete
        del_result = delete_player(user_name, token)
        self.assertIsInstance(del_result, dict)
        self.assertEqual(len(del_result.keys()), 1)
        self.assertIn('message', del_result)
        players = list_players()
        self.assertEqual(len(players), 0)

    def test_players_unique(self):
        user_name = 'test1'
        display_name = "Test user 1"
        create_player(user_name, display_name)
        display_name_2 = "Test user 2"
        try:
            create_player(user_name, display_name_2)
            self.fail()
        except NotAllowed:
            pass

    def test_delete_player_nexist(self):
        self.assertEqual(list_players(), [])
        try:
            delete_player('test1', "asbchjcjkd")
            self.fail()
        except NotFound:
            pass

    def test_delete_player_wrong_token(self):
        self.assertEqual(list_players(), [])
        user_name = 'test1'
        display_name = "Test user 1"
        result = create_player(user_name, display_name)
        token = result['player_token']
        wrong_token = "asbchjcjkd"
        self.assertNotEqual(wrong_token, token)
        try:
            delete_player(user_name, wrong_token)
            self.fail()
        except NotAllowed:
            self.assertEqual(len(list_players()), 1)

from games.api.internal.session import create_session, list_sessions, delete_session
class SessionResourceTests(TestCase):

    fixtures = ["dice"]

    def test_add_delete_session(self):
        game_id = list_games()[0]['id']
        self.assertEqual(list_players(), [])
        # create
        user_name = 'test1'
        display_name = "Test user 1"
        token = create_player(user_name, display_name)['player_token']
        result = create_session(game_id, user_name, token)
        self.assertEqual(len(result.keys()), 2)
        self.assertIn('message', result)
        session_id = result['session_id']
        # get
        sessions = list_sessions()
        self.assertEqual(len(sessions), 1)
        sesh = sessions[0]
        self.assertEqual(len(sesh.keys()), 3)
        self.assertIn('started', sesh)
        self.assertEqual(sesh['creator_id'], user_name)
        self.assertEqual(sesh['game_id'], game_id)
        # delete
        del_result = delete_session(session_id, user_name, token)
        self.assertIsInstance(del_result, dict)
        self.assertEqual(len(del_result.keys()), 1)
        self.assertIn('message', del_result)
        sessions = list_sessions()
        self.assertEqual(len(sessions), 0)

    def test_delete_session_nexist(self):
        self.assertEqual(list_sessions(), [])
        try:
            delete_session('Mario', 'test1', "asbchjcjkd")
            self.fail()
        except NotFound:
            pass

    def test_delete_session_wrong_token(self):
        self.assertEqual(list_players(), [])
        user_name = 'test1'
        display_name = "Test user 1"
        result = create_player(user_name, display_name)
        token = result['player_token']
        wrong_token = "asbchjcjkd"
        self.assertNotEqual(wrong_token, token)
        game_id = list_games()[0]['id']
        session_id = create_session(game_id, user_name, token)['session_id']
        try:
            delete_session(session_id, user_name, wrong_token)
            self.fail()
        except NotAllowed:
            self.assertEqual(len(list_players()), 1)


from games.api.internal.session import adopt_role, list_session_roles
class RoleAdoptionTests(TestCase):

    fixtures = ["dice"]

    def test_adopt_role(self):
        game_id = list_games()[0]['id']
        role_id = list_roles(game_id)[0]['id']
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
        try:
            adopt_role(user_name, role_id, session_id)
        except NotAllowed:
            pass
        roles = list_session_roles(session_id, user_name, token)
        self.assertEqual(len(roles), 1)


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
