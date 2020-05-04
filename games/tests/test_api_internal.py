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
