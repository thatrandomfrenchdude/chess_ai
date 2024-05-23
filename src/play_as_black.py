from chessGame.inputchess import InputChess
from entities.human import player

# setup a chess game
game = InputChess(
    params={
        'testing': False,
        'docker': False
    },
    entities = [player.black]
)

# run the game
game.loop()