# import ai
from move import Move

class Piece():
    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.value = value

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
        return self.color + self.piece_type + " "

class Rook(Piece):
    PIECE_TYPE = "R"
    VALUE = 500

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE, Rook.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def clone(self):
        return Rook(self.x, self.y, self.color)


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


class Bishop(Piece):
    PIECE_TYPE = "B"
    VALUE = 330

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE, Bishop.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_diagonal_moves(board)

    def clone(self):
        return Bishop(self.x, self.y, self.color)


class Queen(Piece):
    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)

    def get_possible_moves(self, board):
        diagonal = self.get_possible_diagonal_moves(board)
        horizontal = self.get_possible_horizontal_moves(board)
        return horizontal + diagonal

    def clone(self):
        return Queen(self.x, self.y, self.color)


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


class Pawn(Piece):
    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)
        self.just_moved_two = False

    def is_starting_position(self):
        return self.y == 1 if self.color == Piece.BLACK else self.y == 6

    def can_en_passant(self, board):
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

    def get_possible_moves(self, board):
        moves = []
        direction = 1 if self.color == Piece.BLACK else -1
        if not board.is_clone:
            print('pawn get possible moves')
            print(self.x, self.y)
            print(direction)
            print(self.can_en_passant(board))
        if board.get_piece(self.x, self.y + direction) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction))

        if self.is_starting_position() and board.get_piece(self.x, self.y + direction) == 0 and board.get_piece(self.x, self.y + direction * 2) == 0:
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        for dx in [-1, 1]:
            piece = board.get_piece(self.x + dx, self.y + direction)
            if piece != 0 and piece.color != self.color:
                moves.append(self.get_move(board, self.x + dx, self.y + direction))
            if self.can_en_passant(board):
                moves.append(self.get_move(board, self.x + dx, self.y + direction))
                print("Appended en passant!")

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)
