# this file contains the list of entities that can play the game

class Entity:
    def __init__(self):
        pass

    @staticmethod
    def get_move():
        raise NotImplementedError
