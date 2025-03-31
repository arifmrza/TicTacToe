import unittest
from unittest.mock import patch
from logic.human import human_player
from logic.board import Board

class TestHumanPlayer (unittest.TestCase):
    def setUp(self):
        self.player = human_player ('X', 'Player 1')
        self.board = Board()

    @patch ('builtins.input', return_value = '1')
    def test_make_move (self, mock_input):
        self.player.make_move (self.board)
        self.assertEqual (self.board.board[0], 'X')

if __name__ == "__main__":
    unittest.main()