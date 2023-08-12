# TODO: add move caching for instant valid move lookup
moveset = {
    'w': {
        'p': [],
        'r': [],
        'n': [],
        'b': [],
        'q': [],
        'k': []
    },
    'b': {
        'p': [],
        'r': [],
        'n': [],
        'b': [],
        'q': [],
        'k': []
    }
}
# for piece on board, check to see if this position has been visited
# if yes, return possible move set
# if no, calculate possible move set and add to moveset

# TODO: add functions to check if move is valid using caching

class Move:
    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto

    # Returns true iff (xfrom,yfrom) and (xto,yto) are the same.
    # def equals(self, other_move):
        # return self.xfrom == other_move.xfrom and self.yfrom == other_move.yfrom and self.xto == other_move.xto and self.yto == other_move.yto
    # Returns true iff (xfrom,yfrom) and (xto,yto) are the same.
    def equals(self, other_move):
        if not isinstance(other_move, Move):
            return False

        return (
            self.xfrom == other_move.xfrom
            and self.yfrom == other_move.yfrom
            and self.xto == other_move.xto
            and self.yto == other_move.yto
        )

    def to_string(self):
        return "(" + self.xpos_to_letter(self.xfrom) + ", " + str(self.yfrom) + ") -> (" + self.xpos_to_letter(self.xto) + ", " + str(self.yto) + ")"
    
    # Converts a letter (A-H) to the x position on the chess board.
    def letter_to_xpos(self, letter):
        letter = letter.upper()
        if letter == 'A':
            return 0
        if letter == 'B':
            return 1
        if letter == 'C':
            return 2
        if letter == 'D':
            return 3
        if letter == 'E':
            return 4
        if letter == 'F':
            return 5
        if letter == 'G':
            return 6
        if letter == 'H':
            return 7

        raise ValueError("Invalid letter.")
    
    def xpos_to_letter(self, xpos):
        if xpos == 0:
            return 'A'
        if xpos == 1:
            return 'B'
        if xpos == 2:
            return 'C'
        if xpos == 3:
            return 'D'
        if xpos == 4:
            return 'E'
        if xpos == 5:
            return 'F'
        if xpos == 6:
            return 'G'
        if xpos == 7:
            return 'H'

        raise ValueError("Invalid xpos.")
