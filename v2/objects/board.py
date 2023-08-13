from objects.pieces.bishop import Bishop
from objects.pieces.king import King
from objects.pieces.knight import Knight
from objects.pieces.pawn import Pawn
from objects.pieces.queen import Queen
from objects.pieces.rook import Rook
from objects.color import Color  # int, 0:1::white:black
from objects.pieces.piece import Piece

class Board:
    WIDTH = 8
    HEIGHT = 8

    # TODO: add board type as input so use has option to select representation
    def __init__(self, chesspieces, white_king_moved, black_king_moved, is_clone=False):
        self.chesspieces = chesspieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved
        self.is_clone = is_clone

    @classmethod
    def clone(cls, b):
        new_pieces = {letter: [0 for _ in range(8)] for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}
        for key, pieces in b.chesspieces.items():
            for i, piece in enumerate(pieces):
                if (piece != 0):
                    new_pieces[key][i] = piece.clone()
        return cls(new_pieces, b.white_king_moved, b.black_king_moved, is_clone=True)

    # creates a new chess board
    @classmethod
    def new(cls, flip=False):
        return cls(cls.hash(), False, False)
    
    # generates a 2d hash table piece board
    @staticmethod
    def hash():
        # hash table representation w/ ordered lists
        pieces = {letter: [0 for _ in range(8)] for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']}

        # Create pawns.        
        for i, letter in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
            pieces[letter][Board.HEIGHT-2] = Pawn(i, Board.HEIGHT-2, Color.WHITE)
            pieces[letter][1] = Pawn(i, 1, Color.BLACK)

        # Create rooks.
        # a0, h0, a7, h7
        pieces['a'][0] = Rook(0, 0, Color.WHITE)
        pieces['h'][0] = Rook(7, 0, Color.WHITE)
        pieces['a'][7] = Rook(0, 7, Color.BLACK)
        pieces['h'][7] = Rook(7, 7, Color.BLACK)

        # Create Knights.
        # b0, g0, b7, g7
        pieces['b'][0] = Knight(1, 0, Color.WHITE)
        pieces['g'][0] = Knight(6, 0, Color.WHITE)
        pieces['b'][7] = Knight(1, 7, Color.BLACK)
        pieces['g'][7] = Knight(6, 7, Color.BLACK)

        # Create Bishops.
        # c0, f0, c7, f7
        pieces['c'][0] = Bishop(2, 0, Color.WHITE)
        pieces['f'][0] = Bishop(5, 0, Color.WHITE)
        pieces['c'][7] = Bishop(2, 7, Color.BLACK)
        pieces['f'][7] = Bishop(5, 7, Color.BLACK)

        # Create King & Queen.
        # d0, e0, d7, e7
        pieces['d'][0] = Queen(3, 0, Color.WHITE)
        pieces['e'][0] = King(4, 0, Color.WHITE)
        pieces['d'][7] = Queen(3, 7, Color.BLACK)
        pieces['e'][7] = King(4, 7, Color.BLACK)

        return pieces
    
    # reset the en passant flags
    def reset_en_passant_flags(self):
        for _, pieces in self.chesspieces.items():
            for piece in pieces:
                if piece and piece.PIECE_TYPE == "P":
                    piece.just_moved_two = False

    # lists all possible moves for a given color on the board --> ai
    def get_possible_moves(self, color):
        moves = []
        for _, pieces in self.chesspieces.items():
            for piece in pieces:
                if piece != 0 and piece.color == color:
                        moves += piece.get_possible_moves(self)
        return moves
    
    # TODO: confirm implementation
    # TODO: implementation for black?
    # TODO: rewrite for hash representation
    def check_en_passant(self, piece, move):
        # delete the pawn that just got passed
        if piece.color == Color.WHITE and \
            ((move.xto - move.xfrom in [-1, 1]) and (move.yto - move.yfrom == 1)):
            self.chesspieces[piece.x][piece.y+1] = 0
        elif piece.color == Color.WHITE and \
            ((move.xto - move.xfrom in [-1, 1]) and (move.yto - move.yfrom == -1)):
            self.chesspieces[piece.x][piece.y-1] = 0
        else:
            pass

    # TODO: rewrite for hash representation
    def perform_move(self, move):
        # save the board state for record
        self.save_board_state()

        # reset en passant flags --> we have a record saved
        # record is saved to game, not board
        self.reset_en_passant_flags()

        # get the piece
        piece = self.chesspieces[move.xfrom][move.yfrom]
        
        # increments piece on the board
        self.move_piece(piece, move.xto, move.yto)

        # check pawn special moves
        if (piece.piece_type == Pawn.PIECE_TYPE):
            # check for en passant
            # en passant validity checked ing pawn.get_possible_moves()
            self.check_en_passant(piece, move)

            # If a pawn reaches the end, upgrade it to a queen.
            if (piece.y == 0 or piece.y == Board.HEIGHT-1):
                self.chesspieces[piece.x][piece.y] = Queen(piece.x, piece.y, piece.color)

        # check king special moves
        if (piece.piece_type == King.PIECE_TYPE):
            # Mark the king as having moved, no more castling.
            if (piece.color == Color.WHITE):
                self.white_king_moved = True
            else:
                self.black_king_moved = True
            
            # Check if king-side castling
            if (move.xto - move.xfrom == 2):
                rook = self.chesspieces[piece.x+1][piece.y]
                self.move_piece(rook, piece.x-1, piece.y)

            # Check if queen-side castling
            if (move.xto - move.xfrom == -2):
                rook = self.chesspieces[piece.x-2][piece.y]
                self.move_piece(rook, piece.x+1, piece.y)

        # check for special board conditions

    
    # updates the state of a piece on the board
    # TODO: rewrite for hash representation
    def move_piece(self, piece, xto, yto):
        if piece != 0:  # added this
            if piece.PIECE_TYPE and abs(yto - piece.y) == 2:
                    piece.just_moved_two = True
            self.chesspieces[piece.x][piece.y] = 0
            piece.x = xto
            piece.y = yto

            self.chesspieces[xto][yto] = piece


    # TODO: rewrite this function
    # TODO: rewrite for hash representation
    def is_check(self, color):
        other_color = Color.WHITE if color == Color.BLACK else Color.BLACK

        for move in self.get_possible_moves(other_color):
            copy = Board.clone(self)
            copy.perform_move(move)

            king_found = False
            for x in range(Board.WIDTH):
                for y in range(Board.HEIGHT):
                    piece = copy.chesspieces[x][y]
                    if piece and piece.color == color and piece.piece_type == King.PIECE_TYPE:
                        king_found = True

            if not king_found:
                print("check")
                return True
        return False

    # Returns piece at given position or 0 if: No piece or out of bounds.
    # TODO: rewrite for hash representation
    def get_piece(self, x, y):
        if (not self.in_bounds(x, y)):
            return 0
        return self.chesspieces[x][y]

    # checks that the given coordinates are within the board spaces
    # TODO: rewrite for hash representation
    def in_bounds(self, x, y):
        return (x >= 0 and y >= 0 and x < Board.WIDTH and y < Board.HEIGHT)

    # converts the board to a string
    def to_string(self, flip):
        return self.black_to_string() if flip else self.white_to_string()
        
    # print with white pieces on the bottom
    # TODO: rewrite for hash representation
    def white_to_string(self):
        string =  "    A  B  C  D  E  F  G  H\n"
        string += "    -----------------------\n"
        for y in range(Board.HEIGHT):
            string += str(8 - y) + " | "
            for x in range(Board.WIDTH):
                piece = self.chesspieces[x][y]
                if (piece != 0):
                    string += piece.to_string()
                else:
                    string += ".. "
            string += "\n"
        return string + "\n"

    
    # print with black pieces on the bottom
    # TODO: rewrite for hash representation
    def black_to_string(self):
        string =  "    H  G  F  E  D  C  B  A\n"
        string += "    -----------------------\n"
        for y in reversed(range(Board.HEIGHT)):
            string += str(8 - y) + " | "
            for x in reversed(range(Board.WIDTH)):
                piece = self.chesspieces[x][y]
                if (piece != 0):
                    string += piece.to_string()
                else:
                    string += ".. "
            string += "\n"
        return string + "\n"

    # returns true or false if there is insufficient material to checkmate
    def is_insuifficient_material(self):
        pass

    def is_fifty_move_rule(self):
        pass
    

