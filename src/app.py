from src.chessGame.autochess import AutoChess
from src.chessGame.inputchess import InputChess
from src.entities.human import player

# add this to chess
# evaluate position
# https://medium.com/@PropelAuth/analyzing-chess-positions-in-python-building-a-chess-analysis-app-part-1-61e6c098f9f3


# class player(Enum):
#     white = 1
#     black = 2


class Game:
    def __init__(self) -> None:
        pass


# basic chess game
def app() -> None:
    # CHESS GAME VARS
    params = {
        'testing': True,
        'docker': False,
    }
    game = None
    players = []
    # options
    # [] is ai
    # [player.white] or [player.black] is human vs ai
    # [player.white, player.black] is human vs human
    game_type = len(players)
    
    # setup the game
    game = AutoChess(
        params=params
    ) if game_type == 0 else InputChess(
        params=params,
        entities=players
    )
    

    # play the game
    game.loop()


if __name__ == '__main__':
    app()