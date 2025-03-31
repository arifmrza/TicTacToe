import unittest
from unittest.mock import patch, MagicMock
from flow.controller import game_controller

class TestGameController (unittest.TestCase):
    def setUp(self):
        self.controller = game_controller()

    @patch ('display.view.game_view.decide_opponent', return_value = 'H')
    def test_choose_opponent_human (self, mock_input):
        self.controller.choose_opponent()
        self.assertEqual (self.controller.model.player1.token, 'X')
        self.assertEqual (self.controller.model.player2.token, 'O')

    @patch ('logic.ai.ai_player')
    @patch ('display.view.game_view.decide_opponent', return_value = 'A')
    def test_choose_opponent_ai (self, mock_input, mock_ai_player):
        mock_ai_player.return_value = MagicMock()
        self.controller.choose_opponent()
        self.assertEqual (self.controller.model.player1.token, 'X')
        self.assertEqual (self.controller.model.player2.token, 'O')


