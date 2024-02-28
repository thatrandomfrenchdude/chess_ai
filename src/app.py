import chess

from src.entities.ai import BestBot
from src.game.autochess import AutoChess

# add this to chess
# evaluate position
# https://medium.com/@PropelAuth/analyzing-chess-positions-in-python-building-a-chess-analysis-app-part-1-61e6c098f9f3


class Game:
    def __init__(self) -> None:
        pass


# basic chess game
def app() -> None:
    # CHESS GAME OPTIONS
    params = {
        'testing': False,
        'docker': False,
    }
    start_pos = chess.STARTING_FEN
    white_agent = BestBot()
    black_agent = BestBot()
    
    # setup the game
    game = AutoChess(
        params=params,
        start_pos=start_pos,
        white_agent=white_agent,
        black_agent=black_agent
    )

    # play the game
    game.loop()


if __name__ == '__main__':
    app()