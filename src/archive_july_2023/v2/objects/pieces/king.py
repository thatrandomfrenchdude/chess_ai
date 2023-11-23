from objects.pieces.piece import Piece
from objects.pieces.rook import Rook
from objects.move_cache import KING

class King(Piece):
    PIECE_TYPE = "K"
    VALUE = 20000

    def __init__(self, letter, num, color):
        super(King, self).__init__(letter, num, color, King.PIECE_TYPE, King.VALUE)

    def get_possible_moves(self):
        moves = KING[self.letter][self.num-1]

        # Add castling moves if in starting position
        if self.letter == 'd' and self.num == 1:
            if self.is_white():
                moves.extend(['b1', 'f1'])
            else:
                moves.extend(['b8', 'f8'])

    def clone(self):
        return King(self.letter, self.num, self.color)

    