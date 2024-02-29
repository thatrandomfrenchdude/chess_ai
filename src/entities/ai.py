from src.entities.entity import Entity

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