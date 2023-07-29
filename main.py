import pieces
from board import Board
from agent import Ai, User

# TODO: add AI vs AI --> need to clean up AI implementation
# TODO: implement en passant
# TODO: convert board represenation to 1D array
# TODO: implement piece lookup table by reference
# TODO: implement lazy evaluation of possible moves + caching to db by state --> valid moves of piece p in position x,y and all other board positions
# TODO: minimize memory usage by eliminating cloning --> bitboard?
# TODO: optimize move generation
# TODO: implement static evaluation function based on board state
# TODO: add ui and api

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

def app() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    app()