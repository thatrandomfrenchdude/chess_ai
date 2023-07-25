import ai
from move import Move

# Converts a letter (A-H) to the x position on the chess board.
def letter_to_xpos(letter):
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

class Agent:
    def __init__(self, color) -> None:
        self.color =  color

    def move(board):
        pass

class Ai(Agent):
    def ai_move(self, board):
        # is this hardcoded to black?
        return ai.AI.get_ai_move(board, self.color, [])

    def move(self, board):
        while True:
            move = self.ai_move(board)
            valid = False
            possible_moves = board.get_possible_moves(self.color)
            # No possible moves
            if (not possible_moves):
                return 0

            for possible_move in possible_moves:
                if (move.equals(possible_move)):
                    valid = True
                    break

            if (valid):
                break
            else:
                print("Invalid move.")
        return move

class User(Agent):
    # Returns a move object based on the users input. Does not check if the move is valid.
    def get_user_move(self):
        print("Example Move: A2 A4")
        move_str = input("Your Move: ")
        move_str = move_str.replace(" ", "")

        try:
            xfrom = letter_to_xpos(move_str[0:1])
            yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
            xto = letter_to_xpos(move_str[2:3])
            yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
            return Move(xfrom, yfrom, xto, yto)
        except ValueError:
            print("Invalid format. Example: A2 A4")
            return self.get_user_move()

    # Returns a valid move based on the users input.
    def move(self, board):
        while True:
            move = self.get_user_move()
            valid = False
            possible_moves = board.get_possible_moves(self.color)
            # No possible moves
            if (not possible_moves):
                return 0

            for possible_move in possible_moves:
                if (move.equals(possible_move)):
                    valid = True
                    break

            if (valid):
                break
            else:
                print("Invalid move.")
        return move