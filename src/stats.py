# references
# https://medium.com/@PropelAuth/analyzing-chess-positions-in-python-building-a-chess-analysis-app-part-1-61e6c098f9f3

# calc most common formations from my games
# learn what to play against
# what do i play? 
# what are better moves?

# provide a prompt
# # TODO: make this better with some chess analysis
# game phases: https://www.chessstrategyonline.com/content/tutorials/basic-chess-concepts-phases-of-the-game

# identify key points where momentum in the game shifted
# momentum is a move that causes the advantage of the game to shift
def game_review():
    pass

import re
import json
import operator
import os

from collections import Counter, defaultdict

from pgn.parsing import *

# goal of this script is to gather stats about games in a file to build a knowledge base

# paths
base_dir: str = os.path.abspath(os.path.join(os.getcwd(), '..'))

# play a pgn game and return the moves and headers
def play_pgn(fp):
    for game in game_generator(fp):
        play_pgn_game(game, delay=1)

def parse_pgn_file(fp):
    # setup function vars
    stats = {
        "1": [], # first move
        "2": [], # second move
        "3": [], # third move
        "4": [], # fourth move
        "5": [], # fifth move
        "6": [], # sixth move
        # "7": [], # seventh move
        # "8": [], # eighth move
        # "9": [], # ninth move
        # "10": [], # tenth move
    }
    games = []
    num_games = 0

    # process each game
    for game in game_generator(fp):
        game_dict = dict(game.headers)
        # handle the moves
        m = [str(m) for m in game.mainline_moves()]
        stats['1'].append((m[0], game_dict['Result']))
        stats['2'].append((''.join(m[0:2]), game_dict['Result']))
        stats['3'].append((''.join(m[0:3]), game_dict['Result']))
        stats['4'].append((''.join(m[0:4]), game_dict['Result']))
        stats['5'].append((''.join(m[0:5]), game_dict['Result']))
        stats['6'].append((''.join(m[0:6]), game_dict['Result']))
        
        game_dict['moves'] = m
        games.append(game_dict)
        num_games += 1

    # return the games and the number of games
    return games, num_games, stats

def process_move_data(dataset):
    # Dictionary to hold counts and win counts for each move
    move_counts = defaultdict(lambda: {'total': 0, 'wins': 0})

    # Aggregate move counts
    for move, result in dataset:
        move_counts[move]['total'] += 1
        # Determine if the result is a win for White
        if result == '1-0':  # White wins
            move_counts[move]['wins'] += 1
        # Optionally handle '0-1' if needed, but here we assume it's always White's perspective

    # Calculate win ratios and sort moves
    move_ratios = {}
    for move, counts in move_counts.items():
        win_ratio = counts['wins'] / counts['total']
        move_ratios[move] = (counts['total'], win_ratio)  # Store total counts and win ratio

    # Sort moves by frequency (total count) in descending order
    sorted_moves = sorted(move_ratios.items(), key=lambda item: item[1][0], reverse=True)

    # Get top 3 moves based on frequency
    top_3_moves = sorted_moves[:3]

    return top_3_moves

def main():
    short_pgn = os.path.join(base_dir, 'short.pgn')
    medium_pgn = os.path.join(base_dir, 'medium.pgn')
    two_pgn = os.path.join(base_dir, 'two.pgn')
    full_pgn = os.path.join(base_dir, 'chess_com_games_2023-11-23.pgn')

    fp = full_pgn

    games, num_games, stats = parse_pgn_file(fp)

    # print the first game
    # print(num_games)
    # print(games[0])

    # # analyze the games in the file here
    # print(num_games)
    # for game in games:
    #     print(game[0])
    #     print(game[1])

    # print(stats)
    # json.dump(stats, open('stats.json', 'w'))

    # top 3 most frequent openings for first 1 to 6 moves
    for key, value in stats.items():
        sorted_moves = process_move_data(value)
        print(f'Top 3 most frequent openings for {key} moves:')
        for move, (total_count, ratio) in sorted_moves:
            print(f'{move} ({total_count} games, {ratio:.2f} win ratio)')
        print()

if __name__ == '__main__':
    main()