from stockfish import Stockfish
from typing import Union

# from config import app_config
from entities import Entity, AIBot
from rules import Rules

# forsyth edwards notation (fen)
# https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
# 1. piece placement from rank 8 to rank 1 separated by /. black is lowercase
# white is uppercase. a number means that many empty squares.
# 2. active color. w or b
# 3. castling availability. KQkq if none then -
# 4. en passant target square in algebraic notation. if none then -
# 5. halfmove clock. number of halfmoves since last capture or pawn advance
# 6. fullmove number. starts at 1 and is incremented after black's move


class Game:
    pass

class Chess(Game):
    def __init__(self,
        start_pos: str = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
        white_agent: Entity() = AIBot(),
        black_agent: Entity() = AIBot()
    ) -> None:
        ### setup chess engine
        self.engine_parameters = {}
        self.stockfish = Stockfish()
        self.stockfish.set_fen_position(start_pos)

        ### game information
        self.white = white_agent
        self.black = black_agent
         # list of moves
        self.moves = []
        # list of board strings
        self.boards = [self.stockfish.get_fen_position()]
        self.halfmoves = 0
        self.fullmoves = 0

        ### player settings

    def choose_mode(self) -> str:
        mode = -1
        while not mode in ['0', '1']:
            mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
        return 'UvA' if mode == '0' else 'AvA'

    def loop(self) -> None:
        try:
            while True:
                # show game board
                print(self.stockfish.get_board_visual())

                # get move and show in console
                self.get_move()
                move = self.moves[-1]
                print(f"Last move: {move}")

                # move evaluation
                # get top n best moves at current position

                # perform move and check conditions
                self.perform_move(move)
                self.halfmoves += 1
                if self.halfmoves % 2 == 0: # black just moved
                    self.fullmoves += 1
        except:
            print("Game Over")

    def get_move(self) -> None:
        move = None
        # check move correct
        # auto checks for white or black based on game state
        while not self.stockfish.is_move_correct(move):
            move = input("Enter a move: ")
        self.moves.append(move)
    
    def perform_move(self, move) -> Union[None, str]:
        # make the move
        self.stockfish.make_moves_from_current_position([move])
        self.boards.append(self.stockfish.get_fen_position())

        # check game conditions
        condition = self.check_game_conditions()
        return condition
        
        
    def check_game_conditions(self) -> Union[None, str]:
        # check
        pass
        # stalemate
        pass
        # checkmate
        pass
        # insufficient material
        if Rules.is_insufficient_material():
            return "insufficient material"
        # 50 move rule
        if Rules.is_fifty_moves(self.halfmoves):
            return "50 move rule"
        # 75 move rule
        if Rules.is_seventyfive_moves(self.halfmoves):
            return "75 move rule"
        # 5 fold repetition
        if Rules.is_fivefold_repetition(self.boards[-1], self.boards):
            return "5 fold repetition"


def app() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    app()