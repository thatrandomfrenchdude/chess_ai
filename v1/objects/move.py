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
        return "(" + str(self.xfrom) + ", " + str(self.yfrom) + ") -> (" + str(self.xto) + ", " + str(self.yto) + ")"
