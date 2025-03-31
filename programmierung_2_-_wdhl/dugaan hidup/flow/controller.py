from logic.game import game_model
from display.view import game_view
from logic.ai import ai_player
from logic.human import human_player
from logic.board import Board

class game_controller:
    def __init__(self):
        self.model = game_model()
        self.view = game_view()
        self.humanplayer = human_player
        self.aiplayer = ai_player
        self.board = Board()

    def game_flow (self):
        while True:#all the function in this will be run
            self.view.welcome_greeting()
            self.choose_opponent()

            if self.model.load_game(): #user will call this function to load the game
                pass
            else:#create a new board if user dont want to load the game
                self.model.board = Board()
                self.model.game_running = True
                self.model.winner = None
                self.model.current_player = self.model.player1

            while self.model.game_running: #the game condition will keep on moving as a loop
                self.view.display_board(self.model.board)

                if isinstance (self.model.current_player, human_player): #if its human move
                    self.model.current_player.make_move (self.model.board)
                elif isinstance (self.model.current_player, ai_player): #if its ai move
                    self.model.current_player.make_move(self.model.board, self.model.board.check_winner, self.view)

                    self.view.display_board (self.model.board)

                if self.model.board.check_winner (self.model.current_player.token): #will check the winner if there is a winner or not yet
                    self.model.winner = self.model.current_player
                    self.model.game_running = False
                    self.view.winner_message (self.model.winner.token)
                    self.view.display_board (self.model.board)
                    break
                elif self.model.board.is_full(): #represent tie cause the board is full but no winner
                    self.model.game_running = False
                    self.view.tie_game()
                    break

                if self.model.save_game(): #if user wanna save game, it will run this function
                   pass
                

                if not self.model.continue_game(): #if user dont want to continue, it will call exit function
                        self.model.exit_game()
                        return
            
              
                    
                if self.model.game_running: #change player after every move
                    self.model.switch_player()

            if not self.model.end_game():
                break


    def choose_opponent (self):
        while True:#loop to keep on going until user chose the right optiom
            opponent_choice = self.view.decide_opponent().upper()
            if opponent_choice == 'H':#vs human
                self.model.player1 = human_player("X", "Player 1")
                self.model.player2 = human_player("O", "Player 2")
                self.model.current_player = self.model.player1
                break
            elif opponent_choice == 'A':#vs ai
                self.model.player1 = human_player("X", "Player")
                self.model.player2 = ai_player("O")
                self.model.current_player = self.model.player1
                break
            else:
                self.view.invalid_gamemode()