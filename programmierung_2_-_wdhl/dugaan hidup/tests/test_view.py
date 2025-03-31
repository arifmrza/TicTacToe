import unittest
from unittest.mock import patch
from display.view import game_view

class TestGameView (unittest.TestCase):
    def setUp(self):
        self.view = game_view()

    @patch ('builtins.print')
    def test_welcome_greeting (self, mock_print):
        self.view.welcome_greeting()
        mock_print.assert_called_once_with ("Welcome to the game !")

    @patch ('builtins.input', return_value = 'H')
    def test_decide_opponent (self, mock_input):
        self.assertEqual (self.view.decide_opponent(), 'H')

    @patch ('builtins.input', return_value = 'y')
    def test_try_load (self, mock_input):
        self.assertEqual (self.view.try_load(), 'Y')

    @patch ('builtins.input', return_value = 'testfile')
    def test_save_file (self, mock_input):
        filename = self.view.save_file()
        self.assertEqual (filename, 'testfile')

    @patch ('builtins.print')
    def test_invalid_move_message (self, mock_print):
        self.view.invalid_move_message()
        mock_print.assert_called_once_with ("Invalid number. Please choose only from 1-9 !")

