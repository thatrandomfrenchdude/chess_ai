import chess
import chess.pgn as cp
import time

# references
# https://python-chess.readthedocs.io/en/latest/pgn.html#


# parses a pgn file and returns a list of games
def parse_pgn_file(pgn_file: str) -> list[cp.Game]:
    games = [game for game in game_generator(pgn_file)]
    return games

# parses a pgn file and returns a generator of games
def game_generator(pgn_file: str) -> cp.Game:
    with open(pgn_file) as f:
        game = cp.read_game(f)
        while game:
            yield game
            game = cp.read_game(f)

# parses a pgn file and returns a generator of moves
def move_generator(game: cp.Game) -> str:
    for move in game.mainline_moves():
        yield move.uci()

# prints a pgn game to console
def play_pgn_game(
    game: cp.Game,
    delay: int = 1
) -> None:
    board = game.board()
    for move in game.mainline_moves():
        board.push(move)
        print(board)
        time.sleep(delay)

# writes a game to a pgn file
def make_pgn(
    self,
    moves: list[str],
    outfile: str = "game.pgn",
    name: str = "game",
    white: str = "white",
    black: str = "black"
):
    if self.moves.count() == 0:
        return None
    
    # add info to the headers
    game = cp.Game()
    game.headers["Event"] = name
    game.headers["White"] = white
    game.headers["Black"] = black
    game.headers["Date"] = time.strftime("%Y.%m.%d")

    def move_generator():
        for move in moves:
            yield move

    # add moves to the game
    for move in move_generator():
        game.add_main_variation(chess.Move.from_uci(move))

    # write the game to a file
    with open(outfile, "w", encoding="utf-8") as f:
        exporter = cp.FileExporter(f)
        game.accept(exporter)