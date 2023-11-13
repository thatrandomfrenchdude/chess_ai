import chess
from stockfish import Stockfish

# from config import app_config
from entities import Entity, BestBot

# forsyth edwards notation (fen)
# https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
# 1. piece placement from rank 8 to rank 1 separated by /. black is lowercase
# white is uppercase. a number means that many empty squares.
# 2. active color. w or b
# 3. castling availability. KQkq if none then -
# 4. en passant target square in algebraic notation. if none then -
# 5. halfmove clock. number of halfmoves since last capture or pawn advance
# 6. fullmove number. starts at 1 and is incremented after black's move

# resources:
# https://medium.com/@PropelAuth/analyzing-chess-positions-in-python-building-a-chess-analysis-app-part-1-61e6c098f9f3
# https://stackoverflow.com/questions/71945463/how-can-i-use-stockfish-in-python-so-that-the-evaluation-is-continuously-updated


class Game:
    pass

class Chess(Game):
    def __init__(self,
        start_pos: str = chess.STARTING_FEN,
        white_agent: Entity() = BestBot(),
        black_agent: Entity() = BestBot()
    ) -> None:
        ### setup chess engine and set to starting position
        self.engine_parameters = {}
        self.engine = Stockfish()
        self.engine.set_fen_position(start_pos)

        ### game information
        self.white = white_agent
        self.black = black_agent
         # list of moves
        self.moves = []
        # list of board strings
        self.board = chess.Board()
        self.boards = [self.board.fen()]
        self.halfmoves = 0
        self.fullmoves = 0

        ### player settings

    def choose_mode(self) -> str:
        mode = -1
        while not mode in ['0', '1']:
            mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
        return 'UvA' if mode == '0' else 'AvA'

    def loop(self) -> None:
        # flag to track game state
        condition = None  # none = normal play

        try:
            while True:
                # show game board
                print(self.board)

                # get move and show in console
                self.get_move()
                move = self.moves[-1]
                print(f"Last move: {move}")

                # move evaluation
                # get top n best moves at current position

                # perform move and check conditions
                condition = self.perform_move(move)
                self.halfmoves += 1
                if self.halfmoves % 2 == 0: # black just moved
                    self.fullmoves += 1

                # check game conditions
                if condition not in [None, "check"]:
                    print(f"Game over: {condition}")
                    break
                elif condition == "check":
                    print("Check")

                # update the chess engine
                self.engine.set_fen_position(self.boards[-1])
        except Exception as e:
            print(f"Exception: {e}")
            print("Game Over")

    # gets a move from the appropriate agent and appends to move list
    def get_move(self) -> None:
        move = self.white.get_move(self.engine) if self.fullmoves % 2 == 0 else self.black.get_move(self.engine)
        self.moves.append(move)
    
    # performs a move in the engine, updates the board list, and checks game conditions
    def perform_move(self, move) -> str | None:
        # TODO: update this to use python chess
        # make the move
        self.board.push_san(move)
        self.boards.append(self.board.fen())

        # check game conditions
        condition = self.check_game_conditions()
        return condition
        
    # checks various conditions that can affect and/or end the game
    def check_game_conditions(self) -> str | None:
        # checkmate - game over
        if self.board.is_checkmate():
            return "checkmate"
        # stalemate - game over
        if self.board.is_stalemate():
            return "stalemate"
        # check - warn player
        if self.board.is_check():
            return "check"
        # insufficient material - draw if neither player can checkmate
        if self.board.is_insufficient_material():
            return "insufficient material"
        # 5 fold repetition - draw after 5 repetitions of the same position
        if self.board.is_fivefold_repetition():
            return "5 fold repetition"
        # 50 move rule - draw after 50 moves without a capture or pawn move
        if self.board.is_fifty_moves():
            return "50 move rule"
        # 75 move rule - draw after 75 moves without a capture or pawn move
        if self.board.is_seventyfive_moves():
            return "75 move rule"


def app() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    app()