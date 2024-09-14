import chess
import chess.engine
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
import logging
import os
import random
import argparse

# Create directories for models and logs
if not os.path.exists('logs'):
    os.makedirs('logs')

if not os.path.exists('models'):
    os.makedirs('models')

# Logging configuration
logging.basicConfig(filename='logs/chess_bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger().addHandler(console)


# --- Configuration Class ---
class Config:
    def __init__(self, epochs=10, n_nodes=5, g_games=10):
        self.epochs = epochs      # Number of epochs
        self.n_nodes = n_nodes    # Number of nodes (bots)
        self.g_games = g_games    # Number of games per bot


# --- Neural Network Model for Chess Bot ---
class ChessBotModel(nn.Module):
    def __init__(self):
        super(ChessBotModel, self).__init__()
        self.fc1 = nn.Linear(773, 128)  # Input size based on chess board representation
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)     # Output a score

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


# --- Bot Manager for Training & Regeneration ---
class BotManager:
    def __init__(self, config):
        self.config = config
        self.bots = [self.create_bot() for _ in range(self.config.n_nodes)]

    def create_bot(self):
        return ChessBotModel()

    def run_epoch(self):
        logging.info(f"Running training for {self.config.epochs} epochs")
        for epoch in range(self.config.epochs):
            results = []
            logging.info(f"Epoch {epoch + 1}/{self.config.epochs}")
            for i in range(self.config.n_nodes):
                bot = self.bots[i]
                bot_wins = 0
                for _ in range(self.config.g_games):
                    opponent = random.choice(self.bots)
                    if opponent is bot:
                        continue
                    result = GameSimulator.play_game(bot, opponent)
                    if result == 1:
                        bot_wins += 1
                results.append((bot, bot_wins))
                logging.info(f"Bot {i + 1}: Won {bot_wins} games")
            winners = GeneticSelector.select_winners(results)
            self.update_weights(winners)
            self.log_progress(epoch, winners)

    def update_weights(self, winners):
        best_weights = GeneticSelector.crossover_weights([w[0].state_dict() for w in winners])
        for bot in self.bots:
            bot.load_state_dict(best_weights)
        logging.info("Weights updated using top-performing bots")

    def log_progress(self, epoch, winners):
        logging.info(f"Epoch {epoch + 1}: Top bot won {winners[0][1]} games")

    def save_model(self, model_path):
        torch.save(self.bots[0].state_dict(), model_path)
        logging.info(f"Model saved to {model_path}")


# --- Game Simulation ---
class GameSimulator:
    @staticmethod
    def play_game(bot1, bot2):
        # Initialize a new chess board
        board = chess.Board()
        while not board.is_game_over():
            if board.turn:
                move = GameSimulator.get_move(bot1, board)
            else:
                move = GameSimulator.get_move(bot2, board)
            if move is None:
                break  # No legal moves available
            board.push(move)

        result = board.result()  # '1-0', '0-1', or '1/2-1/2'
        if result == '1-0':
            return 1  # Bot1 wins
        elif result == '0-1':
            return 0  # Bot2 wins
        else:
            return 0.5  # Draw

    @staticmethod
    def get_move(bot, board):
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return None
        board_tensor = GameSimulator.board_to_tensor(board)
        move_scores = []
        for move in legal_moves:
            board.push(move)
            move_tensor = GameSimulator.board_to_tensor(board)
            score = bot(move_tensor).item()
            move_scores.append(score)
            board.pop()
        best_move = legal_moves[np.argmax(move_scores)]
        return best_move

    @staticmethod
    def board_to_tensor(board):
        # Simplified board representation
        board_state = str(board)
        board_array = []
        piece_map = {
            'P': 1, 'p': -1,
            'N': 2, 'n': -2,
            'B': 3, 'b': -3,
            'R': 4, 'r': -4,
            'Q': 5, 'q': -5,
            'K': 6, 'k': -6,
            '.': 0
        }
        for row in board_state.split('\n'):
            for char in row.split(' '):
                board_array.append(piece_map.get(char, 0))
        # Pad or trim to 773 elements
        board_array = board_array + [0] * (773 - len(board_array))
        return torch.tensor(board_array, dtype=torch.float32)


# --- Genetic Selection & Weight Crossover ---
class GeneticSelector:
    @staticmethod
    def select_winners(results):
        results.sort(key=lambda x: x[1], reverse=True)
        top_n = max(1, int(len(results) / 2))  # Ensure at least one winner
        winners = results[:top_n]
        logging.info(f"Selected top {top_n} bots for weight crossover")
        return winners

    @staticmethod
    def crossover_weights(winner_weights):
        new_weights = {}
        keys = winner_weights[0].keys()
        for key in keys:
            # Initialize with zeros
            new_weights[key] = torch.zeros_like(winner_weights[0][key])
            for weights in winner_weights:
                new_weights[key] += weights[key]
            new_weights[key] /= len(winner_weights)  # Average the weights
        return new_weights


# --- Main Execution ---
if __name__ == '__main__':
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description='Genetic Reinforcement Learning Chess Bot')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--nodes', type=int, default=5, help='Number of nodes (bots)')
    parser.add_argument('--games', type=int, default=10, help='Number of games per bot per epoch')
    args = parser.parse_args()

    # Initialize configuration
    config = Config(epochs=args.epochs, n_nodes=args.nodes, g_games=args.games)

    # Run the bot manager with the given configuration
    bot_manager = BotManager(config)
    bot_manager.run_epoch()

    # Save final model
    bot_manager.save_model('models/final_chess_bot.pth')

    logging.info("Training complete. Final model saved.")
