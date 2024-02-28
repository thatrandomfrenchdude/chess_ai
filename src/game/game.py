import chess
from stockfish import Stockfish
from typing import TypedDict

# from config import app_config
from src.entities.entitiy import Entity
from src.entities.ai import BestBot, AIBot, RLBot
from src.entities.human import User

# resources:
# https://medium.com/@PropelAuth/analyzing-chess-positions-in-python-building-a-chess-analysis-app-part-1-61e6c098f9f3
# https://stackoverflow.com/questions/71945463/how-can-i-use-stockfish-in-python-so-that-the-evaluation-is-continuously-updated
# https://pypi.org/project/stockfish/
# https://github.com/zhelyabuzhsky/stockfish

# desired functionality
# - import one or more pgn files --> for what?
# - train a bot on a set of pgn files --> what does train mean? learn weights model w/ games, fine-tune w/ games, or ?
# - play a game of chess against a bot. at the end of the game, provide analysis
#       i want to get better at chess, and I want interacting with this bot to help me
#       analysis = best moves in key positions with alternate moves and why
#       recognize key patterns --> db of known patterns, generalized
#           train model to recognize probability the next move in a given list of moves match a known pattern
#           and identify which pattern that is. This information can be used to look up analysis.
#           for RL, the machine should then capture the problem-solving method and provide it for grading.
#           graded responses can be used to train the model to explain patterns (teach) better.
# - maintain a record of db of games played to learn from
# - maintain a hash of all moves ever encountered and best move from each position
#       add opening an information from known chess research

class GameParameters(TypedDict):
    testing: bool
    docker: bool


class Chess(Game):
    def __init__(self,
        params: GameParameters,
        start_pos: str,
        white_agent: Entity,
        black_agent: Entity
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

    def choose_mode(self) -> str:
        mode = -1
        while not mode in ['0', '1']:
            mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
        return 'UvA' if mode == '0' else 'AvA'
    
    # returns true if a human is playing
    def is_human_playing(self) -> bool:
        white = True if isinstance(self.white, User) else False
        black = True if isinstance(self.black, User) else False
        return white or black

    def loop(self) -> None:
        raise NotImplementedError

    # gets a move from the appropriate agent and appends to move list
    def get_move(self) -> None:
        move = self.white.get_move(self.engine) if self.halfmoves % 2 == 0 else self.black.get_move(self.engine)
        self.moves.append(move)
    
    # performs a move in the engine, updates the board list, and checks game conditions
    def apply_move(self, move) -> str | None:
        # TODO: update this to use python chess
        # make the move
        self.board.push_san(move)
        self.boards.append(self.board.fen())

        # check game conditions
        condition = self.check_game_conditions()
        return condition
    
    # TODO: use stockfish to evaluate move
    # get top five moves given current position
    # is current move in them?
    # where does it rank if not?
    def evaluate_move(self, move):
        raise NotImplementedError
        
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
