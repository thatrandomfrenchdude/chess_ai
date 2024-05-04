import chess
from stockfish import Stockfish
from typing import TypedDict

# from config import app_config
from src.entities.entity import Entity
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


class Game:
    def __init__(self) -> None:
        pass


class Chess():
    def __init__(self,
        params: GameParameters,
        white: Entity,
        black: Entity,
        start_pos: str = chess.STARTING_FEN
    ) -> None:
        ### buttons and levers
        self.testing = params['testing']

        ### chess engine
        self.engine_parameters = {}
        self.engine = Stockfish()
        self.engine.set_fen_position(start_pos)

        ### game setup
        self.white = white
        self.black = black
        self.board = chess.Board()

        # game state
        self.moves = []
        self.boards = [self.board.fen()]
        self.halfmoves = 0  # even is white, odd is black
        self.fullmoves = 0
    
    # returns true if a human is playing
    def is_human_playing(self) -> bool:
        white = True if isinstance(self.white, User) else False
        black = True if isinstance(self.black, User) else False

        # if a human is playing or testing is on, return true
        return white or black or self.testing
    
    def step(self) -> None:
        pass

    def loop(self) -> None:
        # gameplay vars
        game_condition = "new game"
        human_readable = True if self.is_human_playing() else False
        move_evaluation = True

        # try:
        while True:
            # show game board
            if human_readable:
                print(self.board)

            # get move
            self.get_move()
            move = self.moves[-1]

            # show move in console
            if human_readable:
                if self.halfmoves % 2 == 0:
                    print(f"White move: {move}")
                else:
                    print(f"Black move: {move}")

            # evaluate move
            if move_evaluation:
                print(self.evaluate_move(move, 3, 20, 1000))

            # apply move to board
            game_condition = self.apply_move(move)
            
            # update half and full move counts
            self.halfmoves += 1
            if self.halfmoves % 2 == 0: # black just moved
                self.fullmoves += 1

            # check game conditions
            if game_condition not in [None, "check"]:
                print(f"Game over: {game_condition}")
                break
            elif game_condition == "check" and not self.testing:
                print("Check")

            # update the chess engine
            self.engine.set_fen_position(self.boards[-1])
        # except Exception as e:
            # print("Game ended unexpectedly.")
            # print(f"Exception: {e}")

    # gets a move from the appropriate agent and appends to move list
    def get_move(self) -> None:
        move = self.white.get_move(self.engine) if self.halfmoves % 2 == 0 else self.black.get_move(self.engine)
        self.moves.append(move)
    
    # performs a move in the engine, updates the board list, and checks game conditions
    def apply_move(self, move) -> str | None:
        # TODO: update this to use python chess
        # --> move.uci() to get the move in uci format
        # make the move
        self.board.push_san(move)
        self.boards.append(self.board.fen())

        # check game conditions
        condition = self.check_game_conditions()
        return condition
    
    def evaluate_move(self, move, num_moves, depth_limit=None, time_limit=None) -> list[dict]:
        # get the best moves from the current board --> move has not been applied yet
        # top_move = True if move in best_moves else False
        # if the move is a top move
            # return it to the player along with the better moves
        # if the move is not in the top moves
            # apply the move to the board and evaluate
            # return the top moves and how the move chosen affected the game

        # search_limit = chess.engine.Limit(depth=depth_limit, time=time_limit)
        # info = self.engine.analyse(self.board, search_limit, multipv=num_moves)
        # return [self.format_evaluation(i) for i in info]
        return {}
    
    @staticmethod
    def format_evaluation(info) -> dict:
        # always check from white's perspective
        score = info["score"].white()

        mate_score = score.mate()
        centipawn_score = score.score()
        return {
            "mate_score": mate_score,
            "centipawn_score": centipawn_score,
            "principal_variation": [move.uci() for move in info["pv"]],
        }
        
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
