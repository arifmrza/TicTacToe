import unittest
from logic.ai import ai_player
from logic.board import Board
from unittest.mock import Mock, ANY

class TestAIPlayer (unittest.TestCase):
    def setUp(self):
        self.ai = ai_player ("O")
        self.board = Board()

    def test_ai_make_move (self):
        #mocking the game view object
        mock_view = Mock()

        self.ai.make_move (self.board, self.board.check_winner, mock_view)

        #ensuring the AI's decision is being called 
        mock_view.ai_decision.assert_called_once_with (ANY)

    def test_ai_logic_block (self):
        board_state = ['X', 'X', ' ', ' ', 'O', ' ', ' ', ' ', ' '] #board situation where the human player has a winning chance
        best_move = self.ai.ai_logic (board_state, 0, True, self.board.check_winner)
        self.assertEqual (best_move ['position'], 2) #AI deciding the 2nd index space to block the human's victory

if __name__ == "__main__":
    unittest.main()