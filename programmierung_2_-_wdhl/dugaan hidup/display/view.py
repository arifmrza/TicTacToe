class game_view:

    def welcome_greeting(self):
        print("Welcome to the game !")

    def decide_opponent (self):
        return input ("Enter 'H' to play against human or 'A' to play against AI: ")
    
    def invalid_gamemode (self):
        print ("Invalid choice! Please enter only 'H' or 'A'.")

    def try_load (self):
       return input ("Do you want to load the game? (y/n): ").strip().upper()#strip is to prevent enter or space being taken as input
    
    def try_save (self):
        return input ("Do you want to save the game? (y/n): ").strip().upper()
    
    def try_continue (self):
        return input ("Do you want to continue the game? (y/n): ").strip().upper()

    def display_board (self, board):
        b = board.board
        print (' ' + b[0] + ' | ' + b[1] + ' | ' + b[2])
        print (' ' + b[3] + ' | ' + b[4] + ' | ' + b[5])
        print (' ' + b[6] + ' | ' + b[7] + ' | ' + b[8])

    def winner_message (self, winner):
        print (f"Player {winner} has won !")

    def tie_game (self):
        print ("It's a tie !")

    def game_end (self):
        print ("Game over")

    def game_exit(self):
        print ("Game exited")

    def save_file (self):
        return input ("Enter the filename to save: ")
    
    def load_file (self):
        return input ("Enter the filename to load: ")
    
    def ai_decision (self, move):
        print (f"AI decision box: {move + 1}")

    def invalid_move_message (self):
        print ("Invalid number. Please choose only from 1-9 !")

    def load_game_error(self):
        print("Error: Unable to load the game. Please check the file and try again.")

    def enter_move(self,name):
        return (input(f" {name}, enter your move (1 - 9): "))
    
    def position_taken(self):
        print("Position already taken.")

    def must_choose(self):
        print("Invalid input have been give . Choose Y or N only")

    def value_error (self):
        print ("Invalid input. Please enter a valid number.")