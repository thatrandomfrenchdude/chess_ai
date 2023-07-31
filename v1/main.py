from objects.board import Board
from objects.color import Color
from entities.agent import Ai, User

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
        white = User(Color.WHITE)
        black = Ai(Color.BLACK)
        flip = False
    elif user_color == '1':
        print("user is black")
        white = Ai(Color.WHITE)
        black = User(Color.BLACK)
        flip = True
    return white, black, flip

class Chess():
    def __init__(self) -> None:
        # choose run mode
        # mode = choose_mode()
        mode = 'UvA'

        # define modes
        if mode == 'UvA':
            # self.white_agent, self.black_agent, self.flip = choose_colors()
            self.white_agent = User(Color.WHITE)
            self.black_agent = Ai(Color.BLACK)
            self.flip = False
        elif mode == 'AvA':
            self.white_agent = Ai(Color.WHITE)
            self.black_agent = Ai(Color.BLACK)
            self.flip = False

    def loop(self) -> None:
        # creates a new board and prints it to console
        self.board = Board.new(self.flip)
        print(self.board.to_string())

        while True:
            # get the white move
            # this is returning 0 for some reason
            white_move = self.white_agent.move(self.board)
            print("hello")
            if white_move != 0:
                print(white_move.to_string())
            print("hello")
            if (white_move == 0):
                if (self.board.is_check(Color.WHITE)):
                    print("Checkmate. Black Wins.")
                    break
                else:
                    print("Stalemate.")
                    break

            # perform the move 
            self.board.perform_move(white_move)
            print(self.board.to_string())

            # black move
            black_move = self.black_agent.move(self.board)
            print(black_move)
            if (black_move == 0):
                if (self.board.is_check(Color.BLACK)):
                    print("Checkmate. White wins.")
                    break
                else:
                    print("Stalemate.")
                    break

            # perform the move
            self.board.perform_move(black_move)
            print(self.board.to_string())

def app() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    app()