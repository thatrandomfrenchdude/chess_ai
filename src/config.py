
# from pydantic import BaseModel, BaseSettings


# class EngineConfig(BaseModel):
#     pass


# class AIConfig(BaseModel):
#     def __init__(self):
#         self.infinity = 10000000


# class ChessConfig(BaseSettings):
#     ai_params = AIConfig()
#     engine_params = EngineConfig()

#     class Config:
#         env_file = '.env'
#         env_prefix = 'CHESS_'


# app_config = ChessConfig()