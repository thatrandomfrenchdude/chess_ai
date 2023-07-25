import board, pieces, ai
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

#
# Entry point.
#

# TODO: add agents, user and ai
class Agent:
    def __init__(self, color) -> None:
        self.color =  color

    def move(board):
        pass

class Ai(Agent):
    def ai_move(self, board):
        # is this hardcoded to black?
        ai.AI.get_ai_move(board, [])

    def move(self, board):
        while True:
            move = self.ai_move()
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

# TODO: add AI vs AI

# TODO: ask user to choose a color
# currently user is always white and AI is always black

# 0 for white, 1 for black
user_color = 0

# creates a new board and prints it to console
board = board.Board.new()
print(board.to_string())

user_color = -1
while user_color not in [0, 1]:
    user_color = input("Choose a color, 0 for white, 1 for black")

if user_color == 0:
        # assign agents
        white = User(pieces.Piece.WHITE)
        black = Ai(pieces.Piece.BLACK)
else:
    white = Ai(pieces.Piece.WHITE)
    black = User(pieces.Piece.BLACK)

# program loop
while True:
    # white move
    white_move = white.move(board)
    if (white_move == 0):
        if (board.is_check(pieces.Piece.WHITE)):
            print("Checkmate. Black Wins.")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(white_move)
    print("White move: " + white_move.to_string())
    print(board.to_string())

    # black move
    black_move = black.move(board)
    if (black_move == 0):
        if (board.is_check(pieces.Piece.BLACK)):
            print("Checkmate. White wins.")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(black_move)
    print("AI move: " + black_move.to_string())
    print(board.to_string())
