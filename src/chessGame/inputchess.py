import chess

# from config import app_config
from src.chessGame.chess import Chess as cg, GameParameters
from src.entities.ai import BestBot
from src.entities.human import User, player


class InputChess(cg):
    def __init__(self,
        params: GameParameters,
        entities: list[int],
        start_pos: str = chess.STARTING_FEN,
    ) -> None:
        # setup agents
        white, black = self.setup_agents(entities)

        # setup the super class
        super().__init__(params, white, black, start_pos)

    def setup_agents(self, entities: list[int]) -> str:
        white_agent = User() if player.white in entities else BestBot()
        black_agent = User() if player.black in entities else BestBot()

        return white_agent, black_agent
