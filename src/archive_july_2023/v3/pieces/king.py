class King:
    moves = {
        'a': [
            ['a2', 'b1', 'b2'],
            ['a1', 'a3', 'b1', 'b2', 'b3'],
            ['a2', 'a4', 'b2', 'b3', 'b4'],
            ['a3', 'a5', 'b3', 'b4', 'b5'],
            ['a4', 'a6', 'b4', 'b5', 'b6'],
            ['a5', 'a7', 'b5', 'b6', 'b7'],
            ['a6', 'a8', 'b6', 'b7', 'b8'],
            ['a7', 'b7', 'b8']
        ],
        'b': [
            ['a1', 'a2', 'b2', 'c1', 'c2'],
            ['a1', 'a2', 'a3', 'b1', 'b3', 'c1', 'c2', 'c3'],
            ['a2', 'a3', 'a4', 'b2', 'b4', 'c2', 'c3', 'c4'],
            ['a3', 'a4', 'a5', 'b3', 'b5', 'c3', 'c4', 'c5'],
            ['a4', 'a5', 'a6', 'b4', 'b6', 'c4', 'c5', 'c6'],
            ['a5', 'a6', 'a7', 'b5', 'b7', 'c5', 'c6', 'c7'],
            ['a6', 'a7', 'a8', 'b6', 'b8', 'c6', 'c7', 'c8'],
            ['a7', 'a8', 'b7', 'c7', 'c8']
        ],
        'c': [
            ['b1', 'b2', 'c2', 'd1', 'd2'],
            ['b1', 'b2', 'b3', 'c1', 'c3', 'd1', 'd2', 'd3'],
            ['b2', 'b3', 'b4', 'c2', 'c4', 'd2', 'd3', 'd4'],
            ['b3', 'b4', 'b5', 'c3', 'c5', 'd3', 'd4', 'd5'],
            ['b4', 'b5', 'b6', 'c4', 'c6', 'd4', 'd5', 'd6'],
            ['b5', 'b6', 'b7', 'c5', 'c7', 'd5', 'd6', 'd7'],
            ['b6', 'b7', 'b8', 'c6', 'c8', 'd6', 'd7', 'd8'],
            ['b7', 'b8', 'c7', 'd7', 'd8']
        ],
        'd': [
            ['c1', 'c2', 'd2', 'e1', 'e2'],
            ['c1', 'c2', 'c3', 'd1', 'd3', 'e1', 'e2', 'e3'],
            ['c2', 'c3', 'c4', 'd2', 'd4', 'e2', 'e3', 'e4'],
            ['c3', 'c4', 'c5', 'd3', 'd5', 'e3', 'e4', 'e5'],
            ['c4', 'c5', 'c6', 'd4', 'd6', 'e4', 'e5', 'e6'],
            ['c5', 'c6', 'c7', 'd5', 'd7', 'e5', 'e6', 'e7'],
            ['c6', 'c7', 'c8', 'd6', 'd8', 'e6', 'e7', 'e8'],
            ['c7', 'c8', 'd7', 'e7', 'e8']
        ],
        'e': [
            ['d1', 'd2', 'e2', 'f1', 'f2'],
            ['d1', 'd2', 'd3', 'e1', 'e3', 'f1', 'f2', 'f3'],
            ['d2', 'd3', 'd4', 'e2', 'e4', 'f2', 'f3', 'f4'],
            ['d3', 'd4', 'd5', 'e3', 'e5', 'f3', 'f4', 'f5'],
            ['d4', 'd5', 'd6', 'e4', 'e6', 'f4', 'f5', 'f6'],
            ['d5', 'd6', 'd7', 'e5', 'e7', 'f5', 'f6', 'f7'],
            ['d6', 'd7', 'd8', 'e6', 'e8', 'f6', 'f7', 'f8'],
            ['d7', 'd8', 'e7', 'f7', 'f8']
        ],
        'f': [
            ['e1', 'e2', 'f2', 'g1', 'g2'],
            ['e1', 'e2', 'e3', 'f1', 'f3', 'g1', 'g2', 'g3'],
            ['e2', 'e3', 'e4', 'f2', 'f4', 'g2', 'g3', 'g4'],
            ['e3', 'e4', 'e5', 'f3', 'f5', 'g3', 'g4', 'g5'],
            ['e4', 'e5', 'e6', 'f4', 'f6', 'g4', 'g5', 'g6'],
            ['e5', 'e6', 'e7', 'f5', 'f7', 'g5', 'g6', 'g7'],
            ['e6', 'e7', 'e8', 'f6', 'f8', 'g6', 'g7', 'g8'],
            ['e7', 'e8', 'f7', 'g7', 'g8']
        ],
        'g': [
            ['f1', 'f2', 'g2', 'h1', 'h2'],
            ['f1', 'f2', 'f3', 'g1', 'g3', 'h1', 'h2', 'h3'],
            ['f2', 'f3', 'f4', 'g2', 'g4', 'h2', 'h3', 'h4'],
            ['f3', 'f4', 'f5', 'g3', 'g5', 'h3', 'h4', 'h5'],
            ['f4', 'f5', 'f6', 'g4', 'g6', 'h4', 'h5', 'h6'],
            ['f5', 'f6', 'f7', 'g5', 'g7', 'h5', 'h6', 'h7'],
            ['f6', 'f7', 'f8', 'g6', 'g8', 'h6', 'h7', 'h8'],
            ['f7', 'f8', 'g7', 'h7', 'h8']
        ],
        'h': [
            ['g1', 'g2', 'h2'],
            ['g1', 'g2', 'g3', 'h1', 'h3'],
            ['g2', 'g3', 'g4', 'h2', 'h4'],
            ['g3', 'g4', 'g5', 'h3', 'h5'],
            ['g4', 'g5', 'g6', 'h4', 'h6'],
            ['g5', 'g6', 'g7', 'h5', 'h7'],
            ['g6', 'g7', 'g8', 'h6', 'h8'],
            ['g7', 'g8', 'h7']
        ]
    }
    
    # def __init__(self, color):
    #     self.type = 'k'
    #     self.color = color
    #     self.moved = False

    # def get_possible_moves(self):
    #     return [move for move in self.moves[self.letter][self.number-1] if self.check_move(move)]
    
    # def check_move(self, move):
    #     letter_to = move[0]
    #     number_to = move[1]

    #     # check move is not blocked by same color piece
    #     # check if move "eats" same color piece

    #     return True

    # def to_string(self) -> str:
    #     return f'{self.color}{self.type}'