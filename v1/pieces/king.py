from move import Move
from pieces.piece import Piece
from pieces.rook import Rook

class King(Piece):
    PIECE_TYPE = "K"
    VALUE = 20000

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE, King.VALUE)

    def get_possible_moves(self, board):
        moves = []

        # Add regular king moves
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                moves.append(self.get_move(board, self.x + dx, self.y + dy))

        # Add castling moves
        moves.append(self.get_castle_kingside_move(board))
        moves.append(self.get_castle_queenside_move(board))

        return self.remove_null_from_list(moves)

    # Only checks for castle kingside
    def get_castle_kingside_move(self, board):
        # Are we looking at a valid rook
        piece_in_corner = board.get_piece(self.x+3, self.y)
        if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
            return 0

        # If the rook in the corner is not our color we cannot castle (duh).
        if (piece_in_corner.color != self.color):
            return 0
        
        # If the king has moved, we cannot castle
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        # If there are pieces in between the king and rook we cannot castle
        if (board.get_piece(self.x+1, self.y) != 0 or board.get_piece(self.x+2, self.y) != 0):
            return 0
        
        return Move(self.x, self.y, self.x+2, self.y)

    def get_castle_queenside_move(self, board):
        # Are we looking at a valid rook
        piece_in_corner = board.get_piece(self.x-4, self.y)
        if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
            return 0

        # If the rook in the corner is not our color we cannot castle (duh).
        if (piece_in_corner.color != self.color):
            return 0
        
        # If the king has moved, we cannot castle
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        # If there are pieces in between the king and rook we cannot castle
        if (board.get_piece(self.x-1, self.y) != 0 or board.get_piece(self.x-2, self.y) != 0 or board.get_piece(self.x-3, self.y) != 0):
            return 0
        
        return Move(self.x, self.y, self.x-2, self.y)


    def clone(self):
        return King(self.x, self.y, self.color)