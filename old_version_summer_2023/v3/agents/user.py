from move import Move
from board import Board
from color import Color
from agents.agent import Agent

class User(Agent):
    def __init__(self, color: Color) -> None:
        super().__init__(color)


    def get_move(self) -> str:
        # get move from user
        move = input("Enter move: ").replace(' ', '').lower()

        while not self.check_valid_move(move):
            move = input("Invalid move. Enter move: ").replace(' ', '').lower()

        return Move(move[0], int(move[1]), move[2], int(move[3]))

    # raw user input cleansing
    # check move is two letters and two numbers
    def check_valid_move(self, move) -> bool:
        if len(move) != 4:
            return False
        
        if move[0] not in Board.letters or move[2] not in Board.letters:
            return False

        if not move[1] in range(1,9) or not move[3] in range(1,9):
            return False