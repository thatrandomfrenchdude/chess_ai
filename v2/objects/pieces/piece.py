from objects.move import Move
from objects.color import Color


class Piece():
    def __init__(self, letter: str, num: int, color: int, piece_type: str, value: int):
        self.letter: str = letter
        self.num: int = num
        self.color: int = color # 0 = white, 1 = black
        self.piece_type: str = piece_type
        self.value: int = value

    def is_white(self):
        # notes
        # not 0 = True
        # not 1 = False
        return not self.color

    def get_possible_moves(self):
        pass


    # Returns a Move object with (xfrom, yfrom) set to the piece current position.
    # (letter_to, num_to) is set to the given position. If the move is not valid 0 is returned.
    # A move is not valid if it is out of bounds, or a piece of the same color is
    # being eaten.
    def get_move(self, board, letter_to, num_to):
        move = 0
        if (board.in_bounds(letter_to, num_to)):
            piece = board.get_piece(letter_to, num_to)
            if (piece != 0):
                if (piece.color != self.color):
                    move = Move(self.letter, self.num, letter_to, num_to)
            else:
                move = Move(self.letter, self.num, letter_to, num_to)
        return move

    # Returns the list of moves cleared of all the 0's.
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        return "W" + self.piece_type + " " if self.is_white() else "B" + self.piece_type + " "