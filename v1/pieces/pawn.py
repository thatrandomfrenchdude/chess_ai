# import ai
from pieces.piece import Piece


class Pawn(Piece):
    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)
        self.just_moved_two = False

    def is_starting_position(self):
        return self.y == 1 if self.color == 1 else self.y == 6

    # check if piece to left of pawn has just moved two from starting position
    def en_passant_left(self, board):
        # target_pawn = board.get_piece(x, y)
        piece_left = board.get_piece(self.x - 1, self.y)
        piece_right = board.get_piece(self.x + 1, self.y)
        
        if piece_left == 0 or piece_right == 0:
            return False 
        elif (piece_left.piece_type == Pawn.PIECE_TYPE and piece_left.color != self.color and piece_left.just_moved_two) or \
            (piece_right.piece_type == Pawn.PIECE_TYPE and piece_right.color != self.color and piece_right.just_moved_two):
            print("En passant!")
            return True
        return False
    
    # check if piece to right of pawn has just moved two from starting position
    def en_passant_right(self, board):
        # target_pawn = board.get_piece(x, y)
        piece_left = board.get_piece(self.x - 1, self.y)
        piece_right = board.get_piece(self.x + 1, self.y)
        
        if piece_left == 0 or piece_right == 0:
            return False 
        elif (piece_left.piece_type == Pawn.PIECE_TYPE and piece_left.color != self.color and piece_left.just_moved_two) or \
            (piece_right.piece_type == Pawn.PIECE_TYPE and piece_right.color != self.color and piece_right.just_moved_two):
            print("En passant!")
            return True
        return False
    
    # check en passant to left and right of current pawn
    # def check_en_passant(self, board, move):
    #     left = False
    #     right = False
    #     if self.color == Piece.WHITE:
    #         if self.en_passant_left(board):
    #             # take the piece
    #             # board.chesspieces[self.x - 1][self.y] = 0
    #             left = True
    #         elif self.en_passant_right(board):
    #             # take the piece
    #             # board.chesspieces[self.x + 1][self.y] = 0
    #             right = True
    #     else:
    #         # black
    #         pass
    #     return left, right

    def get_possible_moves(self, board):
        moves = []
        direction = 1 if self.color == 1 else -1
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
        if self.color == 0:
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
