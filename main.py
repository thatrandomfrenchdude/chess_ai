import pieces
from board import Board
from agent import Ai, User

# Reference
# https://towardsdatascience.com/building-a-chess-ai-that-learns-from-experience-5cff953b6784

# TODO: add AI vs AI --> need to clean up AI implementation
# TODO: was able to castle through a knight king/rook fork as black --> illegal
# TODO: was able to move king right two spaces w/o initiating castle

def choose_mode() -> str:
    mode = -1
    while not mode in ['0', '1']:
        mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
    return 'UvA' if mode == '0' else 'AvA'
        

def choose_colors():
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
        # choose run mode
        mode = choose_mode()
        # mode = 'UvA'

        if mode == 'UvA':
            self.white, self.black, self.flip = choose_colors()
            # self.white = Ai(pieces.Piece.WHITE)
            # self.black = User(pieces.Piece.BLACK)
            # self.flip = True
        elif mode == 'AvA':
            self.white = Ai(pieces.Piece.WHITE)
            self.black = Ai(pieces.Piece.BLACK)
            self.flip = False

    def loop(self) -> None:
        # creates a new board and prints it to console
        self.board = Board.new(self.flip)
        print(self.board.to_string())

        while True:
            # get the white move
            white_move = self.white.move(self.board)
            if (white_move == 0):
                if (self.board.is_check(pieces.Piece.WHITE)):
                    print("Checkmate. Black Wins.")
                    break
                else:
                    print("Stalemate.")
                    break

            # perform the move 
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

            # perform the move
            self.board.perform_move(black_move)
            print("Black move: " + black_move.to_string())
            print(self.board.to_string())

def main() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    main()