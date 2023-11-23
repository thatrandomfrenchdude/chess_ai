from multiprocessing import Process
from threading import Thread
from stockfish import Stockfish

# references
# https://pypi.org/project/stockfish/
# https://www.chess.com/blog/raync910/average-centipawn-loss-chess-acpl#:~:text=A%20centipawn%20score%20is%20from,a%20player%20losing%20a%20pawn.


# rl genetic chess network

# chess ai

# chess games

class Competitor:
    def __init__(self):
        # self.games = [Game(RLBot()), AIBot) for _ in range(50)]
        pass
    
    def run(self):
        # rl bot plays 50 games against ai bot as threads in the process
        # threads = [Thread(target=game.run).start().join() for game in self.games]
        pass

class Experiment:
    def __init__(self):
        # self.competitors = [Competitor() for _ in range(10)]
        pass

    def run(self):
        # run each competitor in parallel using processes
        # processes = [Process(target=competitor.run).start().join() for competitor in self.competitors]
        pass

if __name__ == '__main__':
    pass
    # test stockfish
    # stockfish = Stockfish()

    # parameters
    # stockfish.get_parameters()
    # stockfish.update_engine_parameters({})

    # moves = ["e2e4", "e7"e6"]

    # set position as a sequence of moves from starting position
    # stockfish.set_position([])

    # update position with a sequence of moves
    # stockfish.make_moves_from_current_position([])

    # forsyth edwards notation (fen)
    # fen = "rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2"
    # check if fen is valid
    # stockfish.is_valid_fen(fen)
    # stockfish.set_fen_position(fen)
    # stockfish.get_fen_position()

    # get best move
    # stockfish.get_best_move()
    # specify time remaining on clock (in ms)
    # stockfish.get_best_move(wtime=1000, btime=1000)

    # check if move is correct in given position
    # stockfish.is_move_correct("d2d4")

    # get top moves
    # n = 5
    # stockfish.get_top_moves(n)
    # returns a list of dicts

    # get board visual
    # white = true
    # stockfish.get_board_visual(white)

    # position evaluation
    # stockfish.get_evaluation()

    # get item at current square
    # Stockfish.Piece or None
    # stockfish.get_what_is_on_square("e1") # returns Stockfish.Piece.WHITE_KING
    # stockfish.get_what_is_on_square("d8") # returns Stockfish.Piece.BLACK_QUEEN
    # stockfish.get_what_is_on_square("h2") # returns Stockfish.Piece.WHITE_PAWN
    # stockfish.get_what_is_on_square("b5") # returns None

    # find if move will be capture
    # stockfish.will_move_be_a_capture("c3d5")  # returns Stockfish.Capture.DIRECT_CAPTURE  
    # stockfish.will_move_be_a_capture("e5f6")  # returns Stockfish.Capture.DIRECT_CAPTURE  
    # stockfish.will_move_be_a_capture("e5d6")  # returns Stockfish.Capture.EN_PASSANT  
    # stockfish.will_move_be_a_capture("f1e2")  # returns Stockfish.Capture.NO_CAPTURE  

    # StockfishException
    # handles errors with stockfish the object/process
    # does not trigger on all invalid inputs (ie invalid move)
    # from stockfish import StockfishException

    # try:
    #     # Evaluation routine

    # except StockfishException:
    #     # Error handling