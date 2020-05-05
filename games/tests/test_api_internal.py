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


class SessionResourceTests(TestCase):

    def test_create_session(self):
        pass
