from objects.pieces.piece import Piece
from objects.move_cache import ROOK

class Rook(Piece):
    PIECE_TYPE = "R"
    VALUE = 500

    def __init__(self, letter, num, color):
        super(Rook, self).__init__(letter, num, color, Rook.PIECE_TYPE, Rook.VALUE)

    # rook can only move horizontally
    def get_possible_moves(self):
        return ROOK[self.letter][self.num-1]

    def clone(self):
        return Rook(self.letter, self.num, self.color)