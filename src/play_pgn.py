import os

from pgn.parsing import *

base_dir: str = os.path.abspath(os.path.join(os.getcwd(), '..'))
fp = os.path.join(base_dir, 'short.pgn')

for game in game_generator(fp):
    play_pgn_game(game, delay=1)