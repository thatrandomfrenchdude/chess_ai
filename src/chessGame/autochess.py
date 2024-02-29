import chess
from typing import Tuple

# from config import app_config
from src.chessGame.chess import Chess as cg, GameParameters
from src.entities.entity import Entity
from src.entities.ai import BestBot


class AutoChess(cg):
    def __init__(self,
        params: GameParameters,
        start_pos: str = chess.STARTING_FEN,
    ) -> None:
        # setup agents
        white, black = self.setup_agents()
        
        # setup the super class
        super().__init__(params, white, black, start_pos)

    def setup_agents(self) -> Tuple[Entity, Entity]:
        white_agent = BestBot()
        black_agent = BestBot()

        return white_agent, black_agent
