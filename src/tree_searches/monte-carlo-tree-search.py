# references
# https://philippmuens.com/minimax-and-mcts
# https://medium.com/@ishaan.gupta0401/monte-carlo-tree-search-application-on-chess-5573fc0efb75
# code for ^^^: https://github.com/Ish2K/Chess-Bot-AI-Algorithms/blob/main/Git_chess/monte_carlo_implementation.py
# https://www.chessprogramming.org/Monte-Carlo_Tree_Search
# https://ai-boson.github.io/mcts/

# MCST has four steps
#   1. selection -- keep selecting best child until leaf is found
#       formula = wi/ni + c*sqrt(t)/ni
#       wi = number of wins after ith move
#       ni = number of simulations after the ith move
#       c = exploration parameter
#       t = total number of simulations for the parent node
#   2. expansion - when UCT can no longer be applied to find a new successor node,
#   the game tree is expanded by appending all possible states from the leaf node
#   3. rollout (simulation) - picks a child node arbitrarily and simulates the rest of the game
#   until an end state.
#       light play - random nodes are selected for each move
#       heavy play - quality heuristics and eval functions used
#   4. backpropagation - end state reached in previous step is evaluated.
#   traverses upwards back to the root and increments appropriate scores

# Monte Carlo Tree Search

import numpy as np
import chess
import sys
import time
from math import e
from stockfish import Stockfish

# TODO:
# want to make this recursive with stopping conditions I think
# implement a sql database w/ api to store transposition table

# TODO:
# Expand is only being called on the parent node. Need to call it on the children nodes
# as well. This is because the children nodes are not being expanded and the tree is not
# being built out.

# this is where the alpha beta pruning comes in, avoid expanding nodes that are not
# necessary to expand

engine = Stockfish('/opt/homebrew/bin/stockfish')

class MCTS_Node:
    def __init__(self, state, color, parent=None, prev_move=None):
        # node
        self.state = state # the current state of the game in fen format
        self.color = color
        self.number_of_visits = 0 # n 
        self.untried_actions = self.untried_moves(self.state) # actions that have not been tried yet
        self.prev_move = prev_move # the move that led to this state
        
        # relatives
        self.parent: MCTS_Node | None = parent # the parent state of the current state
        self.children: list[MCTS_Node] = [] # children of the current node
        
        # stores the record of the current node as the sum of all subsequent nodes
        self.results = {
            "win": 0, # wins
            "draw": 0, # draws
            "loss": 0 # losses
        }

    @staticmethod
    def untried_moves(state):
        """
        Returns all the untried moves for a given state.
        """
        return list(chess.Board(fen=state).legal_moves)

    def expand(self):
        """
        From the given state, generate all the children provided we are within the
        max search depth as denoted by self.max_depth.

        In this step, all possible child nodes of the generated state are appended
        to the children array and the child node is returned.
        """

        action = self.untried_actions.pop()

        # make a board for the current node to generate the fen for children nodes
        child_board = chess.Board(fen=self.state)

        # apply the move to the board
        child_board.push(action)

        next_state = child_board.fen()

        child_node = MCTS_Node(
            state=next_state,
            color=not self.color,
            parent=self,
            prev_move=action
        )

        # append this to the children of the current node
        self.children.append(child_node)

        # return the new node
        return child_node

        # for move in child_board.legal_moves:
        #     # append the move to the node
        #     self.untried_actions.append(move)
            
        #     # apply the move to the board to get the next state
        #     child_board.push(move)

        #     # get the fen of the new board
        #     child_fen = child_board.fen()

        #     # undo the move
        #     child_board.pop()

        #     # confirm the reset board is the same as the original board
        #     assert self.state == child_board.fen()

        #     # create a new node, passing the board and the parent node
        #     child_node = MCTS_Node(
        #         state = child_fen,
        #         color=not self.color,
        #         parent=self,
        #         prev_move=move
        #     )
        #     self.children.append(child_node)
    
    @staticmethod
    def rollout_policy(board):
        """
        Policy that defines the rollout strategy. Rollout is simulation.
        
        Classical Monte Carlo randomly selects a move from the possible
        moves to play and continues as such until the game is over.

        Can be updated with better policies.
        """
        random = True

        if random:
            # get all the legal moves from this position
            possible_moves = list(board.legal_moves)
            
            # select a move according to the rollout policy
            move = possible_moves[np.random.randint(len(possible_moves))]

            # apply the move to the board
            board.push(move)
        else:
            engine.set_fen_position(board.fen())
            move = engine.get_best_move_time(500)
    
    def rollout(self):
        """
        From the current state, the rest of the game is simulated until completion and the outcome
        of the game is returned.

        Result is returned as 1-0 for white win, 0-1 for black win, and 1/2-1/2 for draw.
        """
        
        # TODO: note running "dozens of games", only single iteration

        # create a board from the fen to use for the rollout
        rollout_board = chess.Board(fen=self.state)

        # while not current_rollout_state.is_game_over():
        while not rollout_board.is_game_over():
            self.rollout_policy(rollout_board)
        
        # get the game result
        result = rollout_board.outcome().result()
        
        # no need to rollback the board as the board is generated from the fen
        # for each rollout that is run

        return result
    
    def backpropagate(self, result) -> None:
        """
        All node statistics are updated until the parent node is reached.

        win/draw/loss results and node visits are incremented.
        """
        self.number_of_visits += 1

        # update the results of the current node
        self.update_results(result)

        if self.parent:
            self.parent.backpropagate(result)
    
    def best_child(self, temp=1):
        """
        Choose the best child is based on the upper confidence bound.

        The first term in the equation is the exploitation, the second
        is the exploration.
        """
        # very small number to prevent division by 0
        tiny_number = 10**-6

        def exploit(child: MCTS_Node):
            return child.get_win_loss() / (child.get_num_visits() + tiny_number)
        
        def explore(child: MCTS_Node):
            return temp * np.sqrt((np.log(self.get_num_visits() + e + tiny_number) / (child.get_num_visits() + tiny_number)))
        
        # calculate the ucb for each child
        ucbs = [exploit(child) + explore(child) for child in self.children]

        # print(f"ucbs: {ucbs}")
        # input("press enter to continue...")
        
        # return the child with the highest ucb
        return self.children[np.argmax(ucbs)]
    
    def tree_policy(self):
        """
        Select the best child node to explore.
        """
        curr_node = self
        while not curr_node.is_terminal_node():
            if not len(curr_node.untried_actions) == 0:
                return curr_node.expand()
            else:
                curr_node = curr_node.best_child()
        return curr_node
    
    # choose the best move to take from
    def best_action(self):
        """
        Returns the node corresponding to the best possible move from a given state.

        This code calls expansion, simulation, and backpropagation.
        """

        simulation_no = 100 # num simulations to run

        # # expand the parent node
        # # TODO: where do I subsequently call expand? only expand as needed
        # self.expand()

        for i in range(simulation_no):

            # select a node from which to run the rollout
            v = self.tree_policy()

            # follow the node to the end of the game using the rollout policy
            reward = v.rollout()

            # backpropagate the result of the rollout through the tree
            v.backpropagate(reward)

        # return the child with the highest number of visits, not just the best child according to ucbs
        # print(f"Number of visits: {self.number_of_visits}")
        # for child in self.children:
        #     print(child.number_of_visits)
        return self.best_child().prev_move
    
    def update_results(self, result):
        """
        Update the results of the current node based on the result of the rollout.
        """
        if result == '1-0':
            if self.color: # true is white
                self.results["win"] += 1
            else:
                self.results["loss"] += 1
        elif result == '0-1':
            if self.color:
                self.results["loss"] += 1
            else:
                self.results["win"] += 1
        else:
            self.results["draw"] += 1
    
    def is_terminal_node(self):
        """
        Used to check if a node is terminal. Terminal node is when the node 
        """
        return True if chess.Board(fen=self.state).is_game_over() else False
    
    def get_win_loss(self):
        """
        Returns the difference between wins and losses
        """
        return self.results["win"] - self.results["loss"]
    
    def get_num_visits(self):
        """
        return the number of times the current node has been visited
        """
        return self.number_of_visits

def best_move(state, color):
    """
    Returns the best move from a given state.
    """
    # run a monte carlo tree search on a given state
    node = MCTS_Node(
        state=state,
        color=color
    )
    next_move = node.best_action()

    return next_move

def one_move():
    """
    Returns the best move from a given position.
    """
    # define an initial state
    initial_state = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1' # starting fen

    # start a chess game form the initial state
    game = chess.Board(fen=initial_state)

    # ai plays as white and returns the best move
    monte_carlo_move = best_move(initial_state, color=game.turn)

    # push the best move to the board
    game.push(monte_carlo_move)

    # print the board and best move
    print(game)
    print(f"Best move: {monte_carlo_move}")

def bot_v_bot():
    """
    Run a game between two monte carlo bots.
    """
    # define an initial state
    initial_state = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1' # starting fen

    # start a chess game form the initial state
    game = chess.Board(fen=initial_state)

    # print the board
    print(f"{game}\n")

    # run the game until it is over
    while not game.is_game_over():
        print("Getting next move...")

        # get the best move for the current player
        start = time.time()
        monte_carlo_move = best_move(game.fen(), color=game.turn)
        end = time.time()

        # push the best move to the board
        game.push(monte_carlo_move)

        # print the board and best move
        print(game)
        print(f"Best move: {monte_carlo_move}")
        print(f"Time taken: {end - start}s\n")

    # print the outcome of the game
    print(f"Game over. {game.result()}")

def test_game():
    # testing to see if start color affects the way outcome is written. No.
    # game = chess.Board(fen='rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1')
    game = chess.Board()
    print(game)
    moves = 0
    while not game.is_game_over():
        move = np.random.choice(list(game.legal_moves))
        game.push(move)
        moves += 1 
    print(game)
    print(f"num moves: {moves}")
    outcome = game.outcome()
    print(f"outcome: {outcome}")
    print(f"result: {game.result()}") # True if White, False if Black
    print(f"winner: {outcome.winner}") # 1-0 means white, 0-1 means black, 1/2-1/2 means draw
    print(f"game over reason: {outcome.termination}")

# def check_function_time(my_func: callable, *args):
#     start = time.time()
#     my_func(*args)
#     end = time.time()
#     print(f"Time taken: {end - start}s")

if __name__ == "__main__":
    start = time.time()
    one_move()
    # test_game()
    # bot_v_bot()
    end = time.time()
    print(f"Total time taken: {int(end - start)}s")