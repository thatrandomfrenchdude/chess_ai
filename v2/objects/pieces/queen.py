from objects.pieces.piece import Piece
from objects.move_cache import QUEEN

class Queen(Piece):
    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, letter, num, color):
        super(Queen, self).__init__(letter, num, color, Queen.PIECE_TYPE, Queen.VALUE)

    def get_possible_moves(self):
        return QUEEN[self.letter][self.num-1]

    def clone(self):
        return Queen(self.letter, self.num, self.color)