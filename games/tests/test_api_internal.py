from django.test import TestCase


from games.api.internal.games import list_games
class GameResourceEmptyTests(TestCase):

    def test_list_empty(self):
        games = list_games()
        self.assertEqual(games, [])


class GameResourceTests(TestCase):

    fixtures = ["dice"]

    def test_list_empty(self):
        games = list_games()
        self.assertEqual(len(games), 1)
        self.assertEqual(games[0], {'id': 'Dice'})


from games.api.internal.players import list_players, create_player, delete_player
from games.api.internal.exceptions import NotAllowed, NotFound
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

    def test_delete_nexist(self):
        self.assertEqual(list_players(), [])
        try:
            delete_player('test1', "asbchjcjkd")
            self.fail()
        except NotFound:
            pass

    def test_delete_wrong_token(self):
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

class SessionResourceTests(TestCase):

    def test_create_session(self):
        pass
