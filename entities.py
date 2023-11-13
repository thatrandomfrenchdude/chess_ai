class Entity:
    def __init__(self):
        pass

    @staticmethod
    def get_move():
        raise NotImplementedError

class User(Entity):
    def __init__(self):
        pass

    @staticmethod
    def get_move(engine):
        move = input("Enter a move: ")
        while not engine.is_move_correct(move):
            move = input("Move invalid. Enter a move: ")
        return move

# generic AI bot
class AIBot(Entity):
    def __init__(self):
        pass
    
# bot always plays the best move in a given position
class BestBot(AIBot):
    def __init__(self):
        pass

    @staticmethod
    def get_move(engine):
        return engine.get_best_move()
    
# plays a move based on RL output
class RLBot(AIBot):
    def __init__(self):
        pass