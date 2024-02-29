from enum import Enum

from src.entities.entity import Entity

class player(Enum):
    white = 1
    black = 2

class User(Entity):
    def __init__(self):
        pass

    @staticmethod
    def get_move(engine):
        move = input("Enter a move: ")
        while not engine.is_move_correct(move):
            move = input("Move invalid. Enter a move: ")
        return move
