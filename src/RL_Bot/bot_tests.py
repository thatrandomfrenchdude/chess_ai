import argparse
import chess
import os
import random
import torch

from chess_bot import BotManager, Config, ChessBotModel, GameSimulator, GeneticSelector

# Testing ChessBotModel
def test_chess_bot_model_forward_pass():
    model = ChessBotModel()
    input_tensor = torch.randn(1, 773)  # Simulating a chess board state
    output = model(input_tensor)
    assert output.shape == (1, 1), "The output shape should be (1, 1)"
    assert torch.is_tensor(output), "The output should be a tensor"

# Testing Config
def test_config_defaults():
    config = Config()
    assert config.epochs == 10, "Default epochs should be 10"
    assert config.n_nodes == 5, "Default n_nodes should be 5"
    assert config.g_games == 10, "Default g_games should be 10"

def test_config_custom():
    config = Config(epochs=20, n_nodes=8, g_games=15)
    assert config.epochs == 20, "Custom epochs should be 20"
    assert config.n_nodes == 8, "Custom n_nodes should be 8"
    assert config.g_games == 15, "Custom g_games should be 15"

# Testing BotManager
def test_bot_manager_initialization():
    config = Config(n_nodes=3)
    manager = BotManager(config)
    assert len(manager.bots) == 3, "There should be 3 bots initialized"

def test_bot_manager_save_model(tmpdir):
    config = Config(n_nodes=3)
    manager = BotManager(config)
    model_path = os.path.join(tmpdir, 'test_model.pth')
    manager.save_model(model_path)
    assert os.path.exists(model_path), "The model should be saved to the specified path"

# Testing GameSimulator
def test_game_simulator_play_game():
    bot1 = ChessBotModel()
    bot2 = ChessBotModel()
    result = GameSimulator.play_game(bot1, bot2)
    assert result in [0, 1, 0.5], "The result should be either 0, 1, or 0.5"

def test_game_simulator_get_move():
    bot = ChessBotModel()
    board = chess.Board()
    move = GameSimulator.get_move(bot, board)
    assert move in board.legal_moves, "The selected move should be a legal move"

# Testing GeneticSelector
def test_genetic_selector_select_winners():
    bots = [(ChessBotModel(), random.randint(0, 10)) for _ in range(5)]
    winners = GeneticSelector.select_winners(bots)
    assert len(winners) == 2, "It should select half the bots as winners"

def test_genetic_selector_crossover_weights():
    bot1 = ChessBotModel().state_dict()
    bot2 = ChessBotModel().state_dict()
    crossover_weights = GeneticSelector.crossover_weights([bot1, bot2])
    assert isinstance(crossover_weights, dict), "Crossover weights should return a dictionary"
    assert all(k in bot1 for k in crossover_weights), "All keys should exist in the new weights"

# Testing argument parsing
def test_argument_parsing(monkeypatch):
    monkeypatch.setattr('sys.argv', ['chess_bot.py', '--epochs', '15', '--nodes', '7', '--games', '12'])
    parser = argparse.ArgumentParser(description='Genetic Reinforcement Learning Chess Bot')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--nodes', type=int, default=5, help='Number of nodes (bots)')
    parser.add_argument('--games', type=int, default=10, help='Number of games per bot per epoch')
    args = parser.parse_args()
    
    assert args.epochs == 15, "The parsed epochs should be 15"
    assert args.nodes == 7, "The parsed nodes should be 7"
    assert args.games == 12, "The parsed games should be 12"
