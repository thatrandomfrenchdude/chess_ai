# this class contains variables and functions for a chess game
from board import Board
from agents.agent import Agent
from typing import Union

class Chess:
    def __init__(self) -> None:
        self.white, self.black = self.setup()
        self.board = Board()
        self.turn = True  # true for white, false for black
        self.moves = []
        self.game_over = False

    def setup(self) -> Union[Agent, Agent]:
        # choose game type --> human vs human, human vs computer, computer vs computer
            # only difference is how moves are generated
        # if at least one human, choose color --> white, black
        pass

    # one step of the game
    def step(self) -> None:
        # get move from player
        move = self.white.get_move() if self.turn else self.black.get_move()

        # check for insufficient material

        # check for 5x same position

        # check for 75+ moves
        if len(self.moves) >= 75:
            self.game_over = True
            print("Draw by 75 move rule.")

        # swap the turn
        self.turn = not self.turn

    # game loop
    def loop(self) -> None:
        while not self.game_over:
            self.step()

def main() -> None:
    game = Chess()
    game.loop()

if __name__ == '__main__':
    main()