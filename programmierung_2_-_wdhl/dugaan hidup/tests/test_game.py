import unittest
from unittest.mock import patch
from logic.game import game_model

class TestGameModel (unittest.TestCase):
    def setUp(self):
        self.model = game_model()

    @patch ('builtins.input', return_value = 'y')
    @patch ('builtins.open')
    def test_save_game (self, mock_open, mock_input):
        self.assertTrue (self.model.save_game())

    @patch ('builtins.input', side_effect = ['y', 'testfile'])
    @patch ('builtins.open')
    def test_load_game (self, mock_open, mock_input):
        self.assertTrue (self.model.load_game())
        mock_open.assert_called_once_with ('testfile', 'r')

if __name__ == "__main__":
    unittest.main()