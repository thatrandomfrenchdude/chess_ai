class Move:
    def __init__(self, letter_from, num_from, letter_to, num_to):
        self.letter_from = letter_from
        self.num_from = num_from
        self.letter_to = letter_to
        self.num_to = num_to

    # Returns true iff (letter_from,num_from) and (letter_to,num_to) are the same.
    # def equals(self, other_move):
        # return self.letter_from == other_move.letter_from and self.num_from == other_move.num_from and self.letter_to == other_move.letter_to and self.num_to == other_move.num_to
    # Returns true iff (letter_from,num_from) and (letter_to,num_to) are the same.
    def equals(self, other_move):
        if not isinstance(other_move, Move):
            return False

        return (
            self.letter_from == other_move.letter_from
            and self.num_from == other_move.num_from
            and self.letter_to == other_move.letter_to
            and self.num_to == other_move.num_to
        )

    def to_string(self):
        return "(" + self.letter_from + ", " + str(self.num_from) + ") -> (" + self.letter_to + ", " + str(self.num_to) + ")"