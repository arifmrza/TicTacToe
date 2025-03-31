import unittest
from logic.player import Player

class TestPlayer (unittest.TestCase):
    def test_token (self):
        player = Player('X')
        self.assertEqual (player.token, 'X')

