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

    # TODO: merge these two functions
    # confirmed working as white with left en passant possible
    # check if piece to left of pawn has just moved two from starting position
    def en_passant_left(self, board):
        # assumes board oriented with white along the bottom
        piece_left = board.get_piece(self.x - 1, self.y)
        
        if piece_left == 0:
            return False 
        else:
            if piece_left.piece_type == Pawn.PIECE_TYPE and \
                piece_left.color != self.color and \
                piece_left.just_moved_two:
                print("En passant left!")
                return True
        return False
    
    # check if piece to right of pawn has just moved two from starting position
    def en_passant_right(self, board):
        # assumes board oriented with white along the bottom
        piece_right = board.get_piece(self.x + 1, self.y)
        
        if piece_right == 0:
            return False 
        elif piece_right.piece_type == Pawn.PIECE_TYPE and piece_right.color != self.color and piece_right.just_moved_two:
            print("En passant right!")
            return True
        return False

    def get_possible_moves(self, board):
        moves = []
        direction = 1 if self.color == Color.BLACK else -1
        if not board.is_clone:
            print('pawn get possible moves')
            print(self.x, self.y)
            print(direction)
            # print(self.can_en_passant(board))
        if board.get_piece(self.x, self.y + direction) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction))

        if self.is_starting_position() and board.get_piece(self.x, self.y + direction) == 0 and board.get_piece(self.x, self.y + direction * 2) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        for dx in [-1, 1]:
            piece = board.get_piece(self.x + dx, self.y + direction)
            if piece != 0 and piece.color != self.color:
                moves.append(self.get_move(board, self.x + dx, self.y + direction))

        # append en passant if applicable
        # TODO: check that these coordinates are correct for left and right
        if self.color == Color.WHITE:
            if self.en_passant_left(board):
                moves.append(self.get_move(board, self.x - 1, self.y - 1))
            if self.en_passant_right(board):
                moves.append(self.get_move(board, self.x + 1, self.y - 1))
        else:
            if self.en_passant_left(board):
                moves.append(self.get_move(board, self.x + 1, self.y + 1))
            if self.en_passant_right(board):
                moves.append(self.get_move(board, self.x - 1, self.y + 1))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)
