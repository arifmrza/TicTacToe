import json
from logic.board import Board
from logic.human import human_player
from logic.ai import ai_player
from display.view import game_view

class game_model:
    def __init__(self):
        self.board = Board()
        self.view = game_view()
        self.player1 = human_player("X", "Player 1")
        self.player2 = ai_player("O")
        self.current_player = self.player1
        self.winner = None
        self.game_running = True

    def switch_player (self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def save_game (self):
        
        response = self.view.try_save()
         #while loop so that it will repeated until intended input is get
        while response not in ['y','Y','n','N']:#making sure that the input only in between these to avoid unintended input
             self.view.must_choose()
             response = self.view.try_save()

        if response in ['y', 'Y']:#is user choose yes to save the game, this data transfer will be conduct and be save as JSON file
             
            filename=self.view.save_file() 
         
            game_state = {
                  'board': self.board.board,
                  'current_player_token': self.current_player.token,
                  'winner': self.winner.token if self.winner else None,
                  'game_running': self.game_running
                }
                 
            with open (filename, 'w') as file:
                  json.dump (game_state, file)

            return True#done saved

        elif response in ['n', 'N']: 
                 return False 
       
        
    
        
        
    def load_game (self):
           
            response = self.view.try_load()
            #same as before to make it in a loop and prevent unintended input
            while response not in ['y','Y','n','N']:
             self.view.must_choose()
             response = self.view.try_load()

            if response in ['y', 'Y']:
                 
             filename=self.view.load_file() 

             try:
               with open (filename, 'r') as file:
                game_state = json.load (file)
                self.board.board = game_state['board']
                self.winner = game_state['winner']
                self.game_running = game_state['game_running']
                current_player_token = game_state['current_player_token']

                if current_player_token == 'X':
                    self.current_player = self.player1
                else:
                    self.current_player = self.player2

             except FileNotFoundError: #some kind of guidance or fallback if there are problems during loading the file
            
              self.view.load_game_error()
             except json.JSONDecodeError :
            
              self.view.load_game_error()
             except Exception :
           
              self.view.load_game_error()

              return True
             
            elif response in ['n', 'N']: 
                 return False 



    def continue_game(self):
        response = self.view.try_continue()

        while response not in ['y','Y','n','N']:
             self.view.must_choose()
             response = self.view.try_continue()

        
        if response in ['y', 'Y']: 
                return True 
        elif response in ['n', 'N']: 
                
                return False 
        

    def exit_game (self):#to exit game if dont want to continue
        game_view.game_exit(self)
        self.game_running = False

    def end_game(self):
        game_view.game_end(self)
        self.game_running = False