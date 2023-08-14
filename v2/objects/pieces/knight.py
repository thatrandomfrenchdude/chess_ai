from objects.pieces.piece import Piece
from objects.move_cache import KNIGHT

class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, letter, num, color):
        super(Knight, self).__init__(letter, num, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self):
        return KNIGHT[self.letter][self.num-1]

    def clone(self):
        return Knight(self.x, self.y, self.color)