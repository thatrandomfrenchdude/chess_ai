# this class contains variable and functions for a chess board

from color import Color
from move import Move

from pieces.king import King
from pieces.queen import Queen
from pieces.rook import Rook
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.pawn import Pawn

class Board:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    def __init__(self) -> None:
        ## VARIABLES ##
        # position of white pieces on the board
        self.white_positions = {
            'p': ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            'r': ['a1', 'h1'],
            'n': ['b1', 'g1'],
            'b': ['c1', 'f1'],
            'q': ['d1'],
            'k': ['e1']
        }
        # position of black pieces on the board
        self.black_positions = {
            'p': ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            'r': ['a8', 'h8'],
            'n': ['b8', 'g8'],
            'b': ['c8', 'f8'],
            'q': ['d8'],
            'k': ['e8']
        }
        # map of the board
        self.pieces = {
            'a': ['wr', 'wp', '', '', '', '', 'bp', 'br'],
            'b': ['wn', 'wp', '', '', '', '', 'bp', 'bn'],
            'c': ['wb', 'wp', '', '', '', '', 'bp', 'bb'],
            'd': ['wq', 'wp', '', '', '', '', 'bp', 'bq'],
            'e': ['wk', 'wp', '', '', '', '', 'bp', 'bk'],
            'f': ['wb', 'wp', '', '', '', '', 'bp', 'bb'],
            'g': ['wn', 'wp', '', '', '', '', 'bp', 'bn'],
            'h': ['wr', 'wp', '', '', '', '', 'bp', 'br']
        }
          # pawns exposed to en passant at current turn
        self.en_passant = []
        # history of the board
        self.history = []

        ## FLAGS ##
        self.white_king_moved = False
        self.black_king_moved = False

        ## ACTIONS ##
        # save the initial board state
        self.save_board()


    # causes one cycle on the board, where one
    # cycle is one player moving a piece.
    def move(self, move: Move) -> None:
        # check if move is valid
        if not self.is_valid_move(move):
            return False
        
        # check en passant if pawn

        # check castling if king

        # perform move
        self.perform_move(move)

        # save move to history
        self.save_board()

    
    # performs a move on the board by updating 
    # board metadata. assumes move is valid and
    # has passed checks.
    def perform_move(self, move: Move) -> None:
        # clear en passant list form previous turn
        self.en_passant = []

        # get the piece to be moved
        piece = self.pieces[move.start[0]][int(move.start[1])-1]
        type = piece[1]
        white = piece.startswith('w')
        
        # update king flags
        if type == 'k':
            if white:
                self.white_king_moved = True
            else:
                self.black_king_moved = True

        # update en passant list
        elif type == 'p':
            # add pawn to en passant list if it moved two spaces
            if abs(int(move.start[1]) - int(move.end[1])) == 2:
                self.en_passant.append(move.end)

        # update the piece in the board map
        self.pieces[move.start[0]][int(move.start[1])-1] = 0
        self.pieces[move.end[0]][int(move.end[1])-1] = piece

        # update the piece in the position lists
        if white:
            self.white_positions[piece.type].remove(move.start)
            self.white_positions[piece.type].append(move.end)
        else:
            self.black_positions[piece.type].remove(move.start)
            self.black_positions[piece.type].append(move.end)
    
    # checks if a given move is valid on the board
    def is_valid_move(self, move: Move) -> bool:
        # set the initial return values
        valid_start = False
        valid_end = True

        # get piece at start position
        piece = self.pieces[move.start[0]][int(move.start[1])-1]
        # get the other pieces of the same color on the board
        pieces = self.white_positions.items() if piece.startswith('w') else self.black_positions.items()
        
        # TODO: add to this -- check for walls etc
        for _, spots in pieces:
            if move.start in spots:
                valid_start = True
            if move.end in spots:
                valid_end = False
            
        return (valid_start and valid_end)


    # return true if color king is in check else false
    def is_check(self, color) -> bool:
        king_pos = self.white_positions['k'][0] if color == Color.white else self.black_positions['k'][0]
        
        for letter in Board.letters:
            for num in range(8):
                if p := self.map[letter][num]:
                    if p.color != color:
                        if king_pos in p.get_possible_moves():
                            return True
        return False
    

    # create a new board history entry
    def save_board(self) -> None:
        record = {
            'board_string': self.encode_state(),
            'white_king_moved': self.white_king_moved,
            'black_king_moved': self.black_king_moved,
            'en_passant': self.en_passant
        }
        self.history.append(record)


    # encodes the current state as a 128 char string
    def encode_state(self) -> str:
        state = ''
        for letter in Board.letters:
            for num in range(8):
                if p := self.pieces[letter][num]:
                    state += p.to_string()
                else:
                    state += '..'
        return state

    # returns a string representation of the board
    @staticmethod
    def to_string(bottom_color: bool, pieces: dict) -> str:
        return Board.white_bottom(pieces) if not bottom_color else Board.black_bottom(pieces)

    # returns a string representation of the board with white on the bottom
    @staticmethod
    def white_bottom(pieces) -> str:
        string =  "    A  B  C  D  E  F  G  H\n"
        string += "    -----------------------\n"
        for num in range(8):
            string += str(num+1) + ' | '
            for letter in Board.letters:
                if p:= pieces[letter][num] != 0:
                    string += p.to_string()
                else:
                    string += '.. '
            string += '\n'
        return string + "    -----------------------\n"

    # returns a string representation of the board with black on the bottom
    @staticmethod
    def black_bottom(pieces) -> str:
        string =  "    H  G  F  E  D  C  B  A\n"
        string += "    -----------------------\n"
        for num in reversed(range(8)):
            string += str(num+1) + ' | '
            for letter in Board.letters:
                if p:= pieces[letter][num] != 0:
                    string += p.to_string()
                else:
                    string += '.. '
            string += '\n'
        return string + "    -----------------------\n"
