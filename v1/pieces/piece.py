from move import Move
from objects.color import Color


class Piece():
    def __init__(self, x: int, y: int, color: int, piece_type: str, value: int):
        self.x: int = x
        self.y: int = y
        self.color: int = color # 0 = white, 1 = black
        self.piece_type: str = piece_type
        self.value: int = value

    def get_possible_moves(self, board):
        pass

    # Returns all diagonal moves for a bishop or queen
    def get_possible_diagonal_moves(self, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        for direction_x, direction_y in directions:
            for i in range(1, 8):
                new_x, new_y = self.x + i * direction_x, self.y + i * direction_y
                if not board.in_bounds(new_x, new_y):
                    break

                piece = board.get_piece(new_x, new_y)
                move = self.get_move(board, new_x, new_y)
                if move:
                    moves.append(move)
                if piece != 0:
                    break

        return moves


    # Returns all horizontal moves for a rook or queen
    def get_possible_horizontal_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for direction_x, direction_y in directions:
            limit = self.x if direction_x != 0 else self.y
            for i in range(1, 8 - limit):
                new_x, new_y = self.x + i * direction_x, self.y + i * direction_y
                piece = board.get_piece(new_x, new_y)
                move = self.get_move(board, new_x, new_y)
                if move:
                    moves.append(move)
                if piece != 0:
                    break

        return self.remove_null_from_list(moves)


    # Returns a Move object with (xfrom, yfrom) set to the piece current position.
    # (xto, yto) is set to the given position. If the move is not valid 0 is returned.
    # A move is not valid if it is out of bounds, or a piece of the same color is
    # being eaten.
    def get_move(self, board, xto, yto):
        move = 0
        if (board.in_bounds(xto, yto)):
            piece = board.get_piece(xto, yto)
            if (piece != 0):
                if (piece.color != self.color):
                    move = Move(self.x, self.y, xto, yto)
            else:
                move = Move(self.x, self.y, xto, yto)
        return move

    # Returns the list of moves cleared of all the 0's.
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        if self.color == Color.WHITE:
            return "W" + self.piece_type + " "
        else:
            return "B" + self.piece_type + " "