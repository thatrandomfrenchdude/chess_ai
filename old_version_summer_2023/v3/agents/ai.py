from color import Color
from agents.agent import Agent

class AI(Agent):
    def __init__(self, color: Color) -> None:
        super().__init__(color)

    # return the best move for the user given the current board
    def get_move(self) -> str:
        # calc_move(board)
        pass
    