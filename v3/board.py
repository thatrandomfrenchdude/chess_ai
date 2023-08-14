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
        self.white_pieces = {
            'p': ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2'],
            'r': ['a1', 'h1'],
            'n': ['b1', 'g1'],
            'b': ['c1', 'f1'],
            'q': ['d1'],
            'k': ['e1']
        }
        self.black_pieces = {
            'p': ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'],
            'r': ['a8', 'h8'],
            'n': ['b8', 'g8'],
            'b': ['c8', 'f8'],
            'q': ['d8'],
            'k': ['e8']
        }
        self.white_king_moved = False
        self.black_king_moved = False

    
    # checks if a given move is valid on the board
    def is_valid_move(self, move: Move, color: Color) -> bool:
        start = False
        end = True
        if not color:  # white
            for _, spots in self.white_pieces.items():
                if move.start in spots
        else:
            for _, v in self.black_pieces.items():
                if move.start not in v:
                    start = False
                if move.end not in v:
                    end = False
        return True


    # return true if color king is in check else false
    def is_check(self, color) -> bool:
        king_pos = self.white_pieces['k'][0] if color == Color.WHITE else self.black_pieces['k'][0]
        
        for letter in Board.letters:
            for num in range(8):
                if p := self.map[letter][num]:
                    if p.color != color:
                        if king_pos in p.get_possible_moves():
                            return True
        return False

    def encode_state(self) -> str:
        state = ''
        for letter in Board.letters:
            for num in range(8):
                if p := self.pieces[letter][num]:
                    state += p.to_string()
                else:
                    state += '..'
        return state

    @staticmethod
    def to_string(bottom_color: bool, pieces: dict) -> str:
        return Board.white_bottom(pieces) if not bottom_color else Board.black_bottom(pieces)

    @staticmethod
    def white_bottom(pieces) -> str:
        string =  "    A  B  C  D  E  F  G  H\n"
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

    @staticmethod
    def black_bottom(pieces) -> str:
        string =  "    H  G  F  E  D  C  B  A\n"
        string += "    -----------------------\n"
