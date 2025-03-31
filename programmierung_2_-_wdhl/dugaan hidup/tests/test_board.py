import unittest
from logic.board import Board

class TestBoard (unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_is_board_full (self):
        self.board.board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O'] #full board situation
        self.assertTrue (self.board.is_full())

    def test_check_winner (self):
        self.board.board = ['X', 'X', 'X', ' ', 'O', ' ', 'O', ' ', ' '] #X player wins
        self.assertTrue (self.board.check_winner('X'))
