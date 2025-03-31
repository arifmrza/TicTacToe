from logic.player import Player
import math

class ai_player (Player):
    def __init__(self, token):
        super().__init__(token)

    def ai_logic (self,board, depth, is_maximizing, check_winner):
        opponent_token = 'X' if self.token == 'O' else 'O'
     

        if check_winner(self.token): #it is for the base case
            return {'position' : None, 'score':10 - depth}
        elif check_winner (opponent_token):
            return {'position' : None, 'score':depth - 10}
        elif ' ' not in board:
            return {'position' : None, 'score':0}
        
        possible_moves = [i for i, letter in enumerate (board) if letter == ' '] #checking the possible move available

        if is_maximizing:
             best = {'position': None, 'score': -math.inf} #AI calculate to maximizing if its own turn

        else:
             best = {'position': None, 'score': math.inf} #AI claculate to minimise if its player turn
        
        
        for move in possible_moves:#AI create every possible end of every moves
            if is_maximizing:
                board[move]= self.token
                sim_score = self.ai_logic (board,depth + 1, False, check_winner)
            else:
                board[move]= opponent_token
                sim_score = self.ai_logic (board, depth + 1, True, check_winner)


            board[move] = ' '
            sim_score['position'] = move

            if is_maximizing:
                if sim_score['score'] > best ['score']: #implementing the max for AI turn
                    best=sim_score

            else:
                if sim_score['score'] < best ['score']: #implementing the min for user turn
                        best = sim_score
        return best

        
    def make_move (self, board, check_winner, game_view):
        current_board = board.board
        best_move = self.ai_logic(current_board,0,True,check_winner)#use the ai logic from above to get the best move
        
        if best_move['position'] is not None:#make the move
            game_view.ai_decision(best_move['position'])
            board.board[best_move['position']] = self.token

     