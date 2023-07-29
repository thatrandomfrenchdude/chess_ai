import sys
import pieces

class Board:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self, chesspieces, white_king_moved, black_king_moved, is_clone=False):
        self.chesspieces = chesspieces
        self.white_king_moved = white_king_moved
        self.black_king_moved = black_king_moved
        self.is_clone = is_clone

    @classmethod
    def clone(cls, chessboard):
        chesspieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = chessboard.chesspieces[x][y]
                if (piece != 0):
                    chesspieces[x][y] = piece.clone()
        return cls(chesspieces, chessboard.white_king_moved, chessboard.black_king_moved, is_clone=True)

    # creates a new chess board
    @classmethod
    def new(cls):
        chess_pieces = [[0 for x in range(Board.WIDTH)] for y in range(Board.HEIGHT)]
        
        # Create pawns.
        for x in range(Board.WIDTH):
            chess_pieces[x][Board.HEIGHT-2] = pieces.Pawn(x, Board.HEIGHT-2, pieces.Piece.WHITE)
            chess_pieces[x][1] = pieces.Pawn(x, 1, pieces.Piece.BLACK)

        # Create rooks.
        chess_pieces[0][Board.HEIGHT-1] = pieces.Rook(0, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[Board.WIDTH-1][Board.HEIGHT-1] = pieces.Rook(Board.WIDTH-1, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[0][0] = pieces.Rook(0, 0, pieces.Piece.BLACK)
        chess_pieces[Board.WIDTH-1][0] = pieces.Rook(Board.WIDTH-1, 0, pieces.Piece.BLACK)

        # Create Knights.
        chess_pieces[1][Board.HEIGHT-1] = pieces.Knight(1, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[Board.WIDTH-2][Board.HEIGHT-1] = pieces.Knight(Board.WIDTH-2, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[1][0] = pieces.Knight(1, 0, pieces.Piece.BLACK)
        chess_pieces[Board.WIDTH-2][0] = pieces.Knight(Board.WIDTH-2, 0, pieces.Piece.BLACK)

        # Create Bishops.
        chess_pieces[2][Board.HEIGHT-1] = pieces.Bishop(2, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[Board.WIDTH-3][Board.HEIGHT-1] = pieces.Bishop(Board.WIDTH-3, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[2][0] = pieces.Bishop(2, 0, pieces.Piece.BLACK)
        chess_pieces[Board.WIDTH-3][0] = pieces.Bishop(Board.WIDTH-3, 0, pieces.Piece.BLACK)

        # Create King & Queen.
        chess_pieces[4][Board.HEIGHT-1] = pieces.King(4, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[3][Board.HEIGHT-1] = pieces.Queen(3, Board.HEIGHT-1, pieces.Piece.WHITE)
        chess_pieces[4][0] = pieces.King(4, 0, pieces.Piece.BLACK)
        chess_pieces[3][0] = pieces.Queen(3, 0, pieces.Piece.BLACK)

        # print the board mask
        # for col in chess_pieces:
        #     print(col)

        # print the white queen object to see piece
        # q = chess_pieces[3][Board.HEIGHT-1]
        # print(q)
        # print(q.piece_type)
        # print(q.color)
        # print(q.x)
        # print(q.y)
        # print(q.value)
        # print(q.get_possible_moves(cls(chess_pieces, False, False)))

        return cls(chess_pieces, False, False)

    # list all possible moves for a given piece at a given position
    def get_possible_moves(self, color):
        moves = []
        for x in range(Board.WIDTH):
            for y in range(Board.HEIGHT):
                piece = self.chesspieces[x][y]
                if (piece != 0):
                    # was
                    # if piece.colo == WHITE:
                    # needs to apply for both colors
                    if (piece.color == color):
                        moves += piece.get_possible_moves(self)

        return moves


    def perform_move(self, move):
        # get the piece
        piece = self.chesspieces[move.xfrom][move.yfrom]
        if not self.is_clone:
            print(piece)
            print(move.xfrom, move.yfrom)
            print(move.xto, move.yto)
            for col in self.chesspieces:
                print(col)
            print('move')
        
        # increments piece on the board
        self.move_piece(piece, move.xto, move.yto)
        if not self.is_clone:
            for col in self.chesspieces:
                print(col)
        # sys.exit()

        # If a pawn reaches the end, upgrade it to a queen.
        if (piece.piece_type == pieces.Pawn.PIECE_TYPE):
            # print('pawn moved')
            if (piece.y == 0 or piece.y == Board.HEIGHT-1):
                self.chesspieces[piece.x][piece.y] = pieces.Queen(piece.x, piece.y, piece.color)

        if (piece.piece_type == pieces.King.PIECE_TYPE):
            if not self.is_clone:
                print('king moved')
            # Mark the king as having moved.
            if (piece.color == pieces.Piece.WHITE):
                self.white_king_moved = True
            else:
                self.black_king_moved = True
            
            # castling works correctly for white
            # TODO: check castling for black
            # Check if king-side castling
            if not self.is_clone:
                print(f"xto: {move.xto} xfrom: {move.xfrom}")
                print(f"to minus from: {move.xto - move.xfrom}")
            if (move.xto - move.xfrom == 2):
                if not self.is_clone:
                    print('king side castling')
                rook = self.chesspieces[piece.x+1][piece.y]
                if not self.is_clone:
                    print(piece, piece.x, piece.y)
                    print(rook)
                self.move_piece(rook, piece.x-1, piece.y)
            # Check if queen-side castling
            if (move.xto - move.xfrom == -2):
                if not self.is_clone:
                    print('queen side castling')
                rook = self.chesspieces[piece.x-2][piece.y]
                self.move_piece(rook, piece.x+1, piece.y)

    
    # why is this needed? --> updates state
    def move_piece(self, piece, xto, yto):
        # print(piece)
        if piece != 0:  # added this
            self.chesspieces[piece.x][piece.y] = 0
            piece.x = xto
            piece.y = yto

            self.chesspieces[xto][yto] = piece


    # Returns if the given color is checked.
    # TODO: make this color agnostic
    # only working for a single color, user is white agent is black
    def is_check(self, color):
        other_color = pieces.Piece.WHITE
        if (color == pieces.Piece.WHITE):
            other_color = pieces.Piece.BLACK

        for move in self.get_possible_moves(other_color):
            copy = Board.clone(self)
            copy.perform_move(move)

            king_found = False
            for x in range(Board.WIDTH):
                for y in range(Board.HEIGHT):
                    piece = copy.chesspieces[x][y]
                    if (piece != 0):
                        if (piece.color == color and piece.piece_type == pieces.King.PIECE_TYPE):
                            king_found = True

            if (not king_found):
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
