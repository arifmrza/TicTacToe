from display.view import game_view
from logic.player import Player

class human_player (Player):
    def __init__(self, token, name):
        super().__init__(token)
        self.name = name
        self.view = game_view()

    def make_move (self, board):
        while True:  #loop to make sure that the right input being insert
            try:
                position = int(self.view.enter_move(self.name))-1
                if not 0 <= position <= 8: #check if the number is correct
                    self.view.invalid_move_message()
                    continue


                if board.board[position] != ' ':
                    position = (self.view.position_taken())

                    continue 

                board.board[position] = self.token
                break

            except ValueError:
                self.view.value_error()