from objects.pieces.piece import Piece
from objects.move_cache import BISHOP

class Bishop(Piece):
    PIECE_TYPE = "B"
    VALUE = 330

    def __init__(self, letter, num, color):
        super(Bishop, self).__init__(letter, num, color, Bishop.PIECE_TYPE, Bishop.VALUE)

    def get_possible_moves(self):
        return BISHOP[self.letter][self.num-1]

    def clone(self):
        return Bishop(self.letter, self.num, self.color)