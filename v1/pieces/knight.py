from pieces.piece import Piece

class Knight(Piece):
    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self, board):
        moves = []
        offsets = [
            (2, 1), (-1, 2), (-2, 1), (1, -2),
            (2, -1), (1, 2), (-2, -1), (-1, -2)
        ]

        for offset_x, offset_y in offsets:
            move = self.get_move(board, self.x + offset_x, self.y + offset_y)
            if move:
                moves.append(move)

        return moves

    def clone(self):
        return Knight(self.x, self.y, self.color)