import chess
import random
from typing import Tuple

class MCTS:
    def __init__(self, root: chess.Board, simulations: int=1000):
        self.root = root
        self.simulations = simulations
        self.tree = {self.board_to_key(root): {"N": 0, "W": 0, "P": None}}

    def board_to_key(self, board: chess.Board) -> str:
        return board.fen()

    def search(self):
        for _ in range(self.simulations):
            node = self.root
            path = [self.board_to_key(node)]

            # Selection
            while self.board_to_key(node) in self.tree and self.tree[self.board_to_key(node)]["P"] is not None:
                node = self.tree[self.board_to_key(node)]["P"]
                path.append(self.board_to_key(node))

            # Expansion
            if self.board_to_key(node) not in self.tree:
                self.tree[self.board_to_key(node)] = {"N": 0, "W": 0, "P": None}
                self.tree[self.board_to_key(node)]["P"] = self.expand(node)

            # Simulation
            result = self.simulate(path[-1])

            # Backpropagation
            for node in reversed(path):
                self.tree[node]["N"] += 1
                self.tree[node]["W"] += result
                if self.tree[node]["P"] is not None:
                    self.tree[node]["P"] = self.uct(node)

    def expand(self, node):
        # Generate all possible moves
        moves = list(node.legal_moves)

        # Randomly select a move
        move = random.choice(moves)

        # Make the move
        next_node = node.copy()
        next_node.push(move)

        return next_node.fen()

    def simulate(self, node):
        # Convert the FEN string to a chess.Board object
        node = chess.Board(node)

        # Simulate a random playout from the given node
        while not node.is_game_over():
            moves = list(node.legal_moves)
            node.push(random.choice(moves))

        # Return the result (1 if white wins, -1 if black wins, 0 if draw)
        return 1 if node.result() == "1-0" else -1 if node.result() == "0-1" else 0

    def uct(self, node):
        # Calculate the UCT value for each child node
        children = [self.tree[node]["P"]] if self.tree[node]["P"] is not None else []
        uct_values = [self.tree[child]["W"] / self.tree[child]["N"] + 2 * (self.simulations / self.tree[child]["N"]) ** 0.5 for child in children]

        # Select the child node with the highest UCT value
        return children[uct_values.index(max(uct_values))]

    def alpha_beta(self, node, alpha, beta, depth):
        best_move_value = -10000
        best_move = None
        
        if self.board_to_key(node) in self.tree and self.tree[self.board_to_key(node)]["P"] is not None:
            return self.tree[self.board_to_key(node)]["P"]

        if node.is_game_over():
            return node.result()

        if depth == 0:
            return self.simulate(self.board_to_key(node))

        moves = list(node.legal_moves)
        for move in moves:
            next_node = node.copy()
            next_node.push(move)

            value = -self.alpha_beta(next_node, -beta, -alpha, depth - 1)
            if value >= beta:
                return value
            alpha = max(alpha, value)
            if value > best_move_value:
                best_move_value = value
                best_move = move

        return best_move_value

    def get_move(self):
        self.search()
        best_move_value = self.alpha_beta(self.root, -10000, 10000, 3)
        best_move = None
        for move in self.root.legal_moves:
            next_node = self.root.copy()
            next_node.push(move)
            value = -self.alpha_beta(next_node, -10000, 10000, 3)
            if value == best_move_value:
                best_move = move
                break
        return best_move
    
    @staticmethod
    def play_game(simulations: int=1000) -> None:
        # Initialize the chess board
        board = chess.Board()

        # Create two MCTS instances for the bots
        bot1 = MCTS(board, simulations)
        bot2 = MCTS(board, simulations)

        # Play the game
        while not board.is_game_over():
            # Bot 1 makes a move
            move = bot1.get_move()
            print("Bot 1:", move)
            board.push(move)

            # Bot 2 makes a move
            move = bot2.get_move()
            print("Bot 2:", move)
            board.push(move)

        # Print the result
        print("Result:", board.result())

# Play a game
MCTS.play_game()