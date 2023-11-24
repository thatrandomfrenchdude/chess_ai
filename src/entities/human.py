from src.entities.entitiy import Entity

class User(Entity):
    def __init__(self):
        pass

    @staticmethod
    def get_move(engine):
        move = input("Enter a move: ")
        while not engine.is_move_correct(move):
            move = input("Move invalid. Enter a move: ")
        return move
