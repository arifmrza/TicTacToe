class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    def is_full (self):
        return ' ' not in self.board
    
    def check_winner (self, token):
        b = self.board
        return (
            (b[0] == token and b[1] == token and b[2] == token) or
            (b[3] == token and b[4] == token and b[5] == token) or
            (b[6] == token and b[7] == token and b[8] == token) or
            (b[0] == token and b[3] == token and b[6] == token) or
            (b[1] == token and b[4] == token and b[7] == token) or
            (b[2] == token and b[5] == token and b[8] == token) or
            (b[0] == token and b[4] == token and b[8] == token) or
            (b[2] == token and b[4] == token and b[6] == token)
        )