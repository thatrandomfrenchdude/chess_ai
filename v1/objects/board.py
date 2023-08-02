from objects.pieces.bishop import Bishop
from objects.pieces.king import King
from objects.pieces.knight import Knight
from objects.pieces.pawn import Pawn
from objects.pieces.queen import Queen
from objects.pieces.rook import Rook
from objects.color import Color

# TODO: add stalemate check on repeats

class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, chesspieces, white_king_moved, black_king_moved, flip, is_clone=False):
        self.chesspieces = chesspieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved
        self.flip = flip
        self.is_clone = is_clone
        
        # save the starting board state
        if not is_clone:
            self.board_state_record = [self.clone(self)]

    @classmethod
    def clone(cls, chessboard):
        chesspieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = chessboard.chesspieces[x][y]
                if (piece != 0):
                    chesspieces[x][y] = piece.clone()
        return cls(chesspieces, chessboard.white_king_moved, chessboard.black_king_moved, False, is_clone=True)

    # creates a new chess board
    @classmethod
    def new(cls, flip=False):
        chess_pieces = [[0 for _ in range(Board.WIDTH)] for _ in range(Board.HEIGHT)]
        
        # Create pawns.
        for x in range(Board.WIDTH):
            chess_pieces[x][Board.HEIGHT-2] = Pawn(x, Board.HEIGHT-2, Color.WHITE)
            chess_pieces[x][1] = Pawn(x, 1, Color.BLACK)

        # Create rooks.
        chess_pieces[0][Board.HEIGHT-1] = Rook(0, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[Board.WIDTH-1][Board.HEIGHT-1] = Rook(Board.WIDTH-1, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[0][0] = Rook(0, 0, Color.BLACK)
        chess_pieces[Board.WIDTH-1][0] = Rook(Board.WIDTH-1, 0, Color.BLACK)

        # Create Knights.
        chess_pieces[1][Board.HEIGHT-1] = Knight(1, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[Board.WIDTH-2][Board.HEIGHT-1] = Knight(Board.WIDTH-2, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[1][0] = Knight(1, 0, Color.BLACK)
        chess_pieces[Board.WIDTH-2][0] = Knight(Board.WIDTH-2, 0, Color.BLACK)

        # Create Bishops.
        chess_pieces[2][Board.HEIGHT-1] = Bishop(2, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[Board.WIDTH-3][Board.HEIGHT-1] = Bishop(Board.WIDTH-3, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[2][0] = Bishop(2, 0, Color.BLACK)
        chess_pieces[Board.WIDTH-3][0] = Bishop(Board.WIDTH-3, 0, Color.BLACK)

        # Create King & Queen.
        chess_pieces[4][Board.HEIGHT-1] = King(4, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[3][Board.HEIGHT-1] = Queen(3, Board.HEIGHT-1, Color.WHITE)
        chess_pieces[4][0] = King(4, 0, Color.BLACK)
        chess_pieces[3][0] = Queen(3, 0, Color.BLACK)

        return cls(chess_pieces, False, False, flip)
    
    # reset the en passant flags
    def reset_en_passant_flags(self):
        for row in self.chesspieces:
            for piece in row:
                if piece and piece.PIECE_TYPE == "P":
                    piece.just_moved_two = False

    # save the current board state
    def save_board_state(self):
        if not self.is_clone:
            self.board_state_record.append(self.clone(self))

    # lists all possible moves for a given color on the board
    # TODO: remove this function
    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.chesspieces[x][y]
                if piece != 0:
                    if piece.color == color:
                        moves += piece.get_possible_moves(self)
        return moves
    
    # TODO: confirm implementation
    # TODO: implementation for black?
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

    def perform_move(self, move):
        # reset en passant flags --> we have a record saved
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

        # save the board state for record
        self.save_board_state()

    
    # updates the state of a piece on the board
    def move_piece(self, piece, xto, yto):
        if piece != 0:  # added this
            if piece.PIECE_TYPE and abs(yto - piece.y) == 2:
                    piece.just_moved_two = True
            self.chesspieces[piece.x][piece.y] = 0
            piece.x = xto
            piece.y = yto

            self.chesspieces[xto][yto] = piece


    # TODO: rewrite this function
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
    def get_piece(self, x, y):
        if (not self.in_bounds(x, y)):
            return 0
        return self.chesspieces[x][y]

    # checks that the given coordinates are within the board spaces
    def in_bounds(self, x, y):
        return (x >= 0 and y >= 0 and x < Board.WIDTH and y < Board.HEIGHT)

    # converts the board to a string
    def to_string(self):
        if self.flip:
            return self.black_to_string()
        else:
            return self.white_to_string()
        
    # print with white pieces on the bottom
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
