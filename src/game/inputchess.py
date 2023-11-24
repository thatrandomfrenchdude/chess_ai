import chess
from stockfish import Stockfish

# from config import app_config
from src.game.game import Chess as cg
from src.entities.entitiy import Entity
from src.entities.ai import BestBot
from src.entities.human import User


class InputChess(cg):
    def __init__(self,
        params: dict = {
            'testing': False,
            'docker': False,
        },
        start_pos: str = chess.STARTING_FEN,
        white_agent: Entity() = User(),
        black_agent: Entity() = BestBot()
    ) -> None:
        # buttons and levers
        self.testing = params['testing']

        ### chess engine
        self.engine_parameters = {}
        self.engine = Stockfish()
        self.engine.set_fen_position(start_pos)

        ### game setup
        self.white = white_agent
        self.black = black_agent
        self.board = chess.Board()

        # game state
        self.moves = []
        self.boards = [self.board.fen()]
        self.halfmoves = 0  # even is white, odd is black
        self.fullmoves = 0

        ### player settings
    
    def loop(self) -> None:
        # flag to track game state
        condition = None  # none = normal play

        try:
            while True:
                # show game board
                if not self.testing:
                    print(self.board)

                # get move and show in console
                self.get_move()
                move = self.moves[-1]
                if not self.testing:
                    print(f"Last move: {move}")

                # move evaluation
                # get top n best moves at current position
                # where does current move rank?
                # if not in top n, warn player
                # how do I know if this is a player or bot?
                # only analyze if player is a user
                if self.halfmoves % 2 == 0:
                    if isinstance(self.white, User):
                        self.evaluate_move(move) # white just moved
                else:
                    if isinstance(self.black, User):
                        self.evaluate_move(move) # black just moved

                # perform move and check conditions
                condition = self.apply_move(move)
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
    
    # TODO: use stockfish to evaluate move
    # get top five moves given current position
    # is current move in them?
    # where does it rank if not?
    def evaluate_move(self, move):
        raise NotImplementedError
