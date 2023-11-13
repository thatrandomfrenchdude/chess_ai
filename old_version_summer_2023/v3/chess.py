# this class contains variables and functions for a chess game
from board import Board
from agents.agent import Agent
from agents.user import User
from typing import Union, Optional
from color import Color

class Chess:
    def __init__(self) -> None:
        # generate a new board
        self.board = Board()

        # setup the game
        self.white, self.black = self.setup()
        
        self.turn = True  # true for white, false for black
        self.moves = []
        self.game_over = False
        self.flip = False
        self.mode: Optional[str] = None
        self.white: Optional[Agent] = None
        self.black: Optional[Agent] = None

    # takes in user input to decide game mode
    # options: User v AI, AI v AI
    def choose_mode(self) -> str:
        mode = -1
        while not mode in ['0', '1']:
            mode = input("Choose a game mode, 0 user vs ai, 1 for ai vs ai: ")
        return 'UvA' if mode == '0' else 'AvA'

    def choose_colors(self) -> bool:
        user_color = -1
        while not user_color in ['0', '1']:
            user_color = input("Choose a color, 0 for white, 1 for black: ")
        return False if user_color == '0' else True

    def setup(self) -> None:
        # choose game type --> human vs human, human vs computer, computer vs computer
        self.mode = self.choose_mode()
        
        if self.mode == 'UvA':
            if not self.choose_colors():
                self.white = User(Color.white, self.board)
                self.black = User(Color.black, self.board)
            else:
                self.white = User(Color.white, self.board)
                self.black = User(Color.black, self.board)
                self.flip = True

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
    game.setup()
    game.loop()

if __name__ == '__main__':
    main()