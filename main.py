import pieces
from board import Board
from agent import Ai, User, Agent

# TODO: create a session --> game: board, white, black
# TODO: add AI vs AI

def choose_mode() -> str:
    mode = -1
    while not mode in ['0', '1']:
        mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
    return 'UvA' if mode == 1 else 'AvA'
        

def choose_colors() -> tuple(Agent, Agent, bool):
    user_color = -1
    while not user_color in ['0', '1']:
        user_color = input("Choose a color, 0 for white, 1 for black: ")

    if user_color == '0':
        print('user is white')
        white = User(pieces.Piece.WHITE)
        black = Ai(pieces.Piece.BLACK)
        flip = False
    elif user_color == '1':
        print("user is black")
        white = Ai(pieces.Piece.WHITE)
        black = User(pieces.Piece.BLACK)
        flip = True
    return white, black, flip

class Chess():
    def __init__(self) -> None:
        # creates a new board and prints it to console
        self.board = Board.new()
        print(self.board.to_string())

        # choose run mode
        mode = choose_mode()

        if mode == 'UvA':
            self.white, self.black, self.flip = choose_colors()
        elif mode == 'AvA':
            self.white = Ai(pieces.Piece.WHITE)
            self.black = Ai(pieces.Piece.BLACK)
            self.flip = False

        # flip board when playing as black
        if self.flip:
            pass

    def loop(self) -> None:
        while True:
            # white move
            white_move = self.white.move(self.board)
            if (white_move == 0):
                if (self.board.is_check(pieces.Piece.WHITE)):
                    print("Checkmate. Black Wins.")
                    break
                else:
                    print("Stalemate.")
                    break

            self.board.perform_move(white_move)
            print("White move: " + white_move.to_string())
            print(self.board.to_string())

            # black move
            black_move = self.black.move(self.board)
            if (black_move == 0):
                if (self.board.is_check(pieces.Piece.BLACK)):
                    print("Checkmate. White wins.")
                    break
                else:
                    print("Stalemate.")
                    break

            self.board.perform_move(black_move)
            print("AI move: " + black_move.to_string())
            print(self.board.to_string())

def main() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    main()