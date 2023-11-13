# import ai
from objects.pieces.piece import Piece
from objects.color import Color


class Pawn(Piece):
    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)
        self.just_moved_two = False

    def is_starting_position(self):
        return self.y == 1 if self.color == Color.BLACK else self.y == 6

    # checks to see if en passant is possible
    # returns a list with a move for each side if possible
    def en_passant(self, board):
        ans = []

        # get the x values to the left and right of the pawn
        l_x = self.x - 1 if self.is_white() else self.x + 1
        r_x = self.x + 1 if self.is_white() else self.x - 1

        # get the pieces around the pawn
        l_piece = board.get_piece(l_x, self.y)
        r_piece = board.get_piece(r_x, self.y)

        # TODO: check last state for just moved two
        if self.en_passant_left(l_piece):
            ans.append(self.get_move(board, l_x, self.y - 1 if self.is_white() else self.y + 1))
        if self.en_passant_right(r_piece):
            ans.append(self.get_move(board, r_x, self.y - 1 if self.is_white() else self.y + 1))

        return ans

    def en_passant_left(self, piece):
        # make sure there is a piece to the left
        if piece == 0:
            return False 
        else:
            if piece.piece_type == Pawn.PIECE_TYPE and \
                piece.color is not self.color and \
                piece.just_moved_two:
                # print("En passant left is possible!")
                return True
        return False
    
    def en_passant_right(self, piece):
        # make sure there is a piece to the right
        if piece == 0:
            return False 
        else:
            if piece.piece_type == Pawn.PIECE_TYPE and \
                piece.color is not self.color and \
                piece.just_moved_two:
                # print("En passant right is possible!")
                return True
        return False


    def get_possible_moves(self, board):
        moves = []
        direction = 1 if self.color == Color.BLACK else -1
        if board.get_piece(self.x, self.y + direction) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction))

        if self.is_starting_position() and board.get_piece(self.x, self.y + direction) == 0 and board.get_piece(self.x, self.y + direction * 2) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        for dx in [-1, 1]:
            piece = board.get_piece(self.x + dx, self.y + direction)
            if piece != 0 and piece.color != self.color:
                moves.append(self.get_move(board, self.x + dx, self.y + direction))

        # append en passant if applicable
        moves.extend(self.en_passant(board))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)
    