class Move:
    def __init__(self, start: str, end: str):
        self.start = start
        self.end = end

    def equals(self, other_move):
        if not isinstance(other_move, Move):
            return False

        return (
            self.start == other_move.start
            and self.end == other_move.end
        )
    
    def to_string(self):
        return f'{self.start} -> {self.end}'
    