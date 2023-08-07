from objects.board import Board
from objects.color import Color
from entities.user import User
from entities.ai import Ai

# Outstanding work, grouped by similarity

# TODO: add testing framework to test all possible moves
# TODO: add testing to ensure 

# TODO: implement move cache --> when calculating valid moves of a piece from a spot, save these for later use
# TODO: implement lazy evaluation of possible moves + caching to db by state --> valid moves of piece p in position x,y and all other board positions

# BUG: resolve AI v AI gets stuck in repeating moves
# TODO: refactor/optimize move generation:
    # 1. apply move rules for piece to gen list possible moves.
    # 2. overlay on board to check bounds + blocked.
    # 3. return true/false

# TODO: minimize memory usage by eliminating cloning --> bitboard?
# TODO: implement static evaluation function based on board state

# TODO: add ui and api

# BUG: unable to take queen with my queen, invalid move
# d2 -> d4, d4 -> d5, e2 -> e4, f2 -> f3, d5 -> c6, d1 -> d8


class Chess():
    def __init__(self) -> None:
        # generate a new board (we always need one)
        flip = False  # always default to false
        self.board = Board.new(flip)
        self.move_history = []

        # choose run mode
        mode = self.choose_mode()
        # mode = 'UvA'

        # define modes
        if mode == 'UvA':
            if not self.choose_colors():
                self.white_agent = User(Color.WHITE, self.board)
                self.black_agent = Ai(Color.BLACK, self.board)
            else:
                self.white_agent = Ai(Color.WHITE, self.board)
                self.black_agent = User(Color.BLACK, self.board)
                self.flip = True
        elif mode == 'AvA':
            self.white_agent = Ai(Color.WHITE, self.board)
            self.black_agent = Ai(Color.BLACK, self.board)

    # takes in user input to decide game mode
    def choose_mode(self) -> str:
        mode = -1
        while not mode in ['0', '1']:
            mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
        return 'UvA' if mode == '0' else 'AvA'
    
    # takes in user input to decide use and ai colors
    def choose_colors(self) -> bool:
        user_color = -1
        while not user_color in ['0', '1']:
            user_color = input("Choose a color, 0 for white, 1 for black: ")
        return False if user_color == '0' else True

    def loop(self) -> None:
        try:
            # print board to console
            print(self.board.to_string())

            while True:
                # get the white move
                white_move = self.white_agent.move()
                print(white_move.to_string())
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
                black_move = self.black_agent.move()
                print(black_move.to_string())
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
        except:
            print("Game Over")
            self.print_game_record()
        
    def print_game_record(self) -> None:
        for state in self.board.board_state_record:
            # print(state.to_string())
            print(state)

def app() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    app()