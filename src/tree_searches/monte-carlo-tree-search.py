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

# TODO:
# want to make this recursive with stopping conditions I think
# implement a sql database w/ api to store transposition table

# TODO:
# Expand is only being called on the parent node. Need to call it on the children nodes
# as well. This is because the children nodes are not being expanded and the tree is not
# being built out.

# this is where the alpha beta pruning comes in, avoid expanding nodes that are not
# necessary to expand

class MCTS_Node:
    def __init__(self, state, color, parent=None, max_depth=3):
        # node
        self.state = state # the current state of the game in fen format
        self.max_depth = max_depth # the maximum depth of the tree
        self.color = color
        
        # relatives
        self.parent: MCTS_Node | None = parent # the parent state of the current state
        self.children: list[MCTS_Node] = [] # children of the current node

        # the number of times the current node has been visited
        self.number_of_visits = 0
        
        # stores the record of the current node as the sum of all subsequent nodes
        self.results = {
            "win": 0, # wins
            "draw": 0, # draws
            "loss": 0 # losses
        }

    def expand(self):
        """
        From the given state, generate all the children provided we are within the
        max search depth as denoted by self.max_depth.

        In this step, all possible child nodes of the generated state are appended
        to the children array and the child node is returned.
        """

        # make a board for the curren node to generate the fen for children nodes
        child_board = chess.Board(fen=self.state)

        for move in child_board.legal_moves:
            # apply the move to the board
            child_board.push(move)

            # get the fen of the new board
            child_fen = child_board.fen()

            # undo the move
            child_board.pop()

            # confirm the reset board is the same as the original board
            assert self.state == child_board.fen()

            # create a new node, passing the board and the parent node
            child_node = MCTS_Node(
                child_fen,
                color=not self.color,
                parent=self,
                max_depth=self.max_depth - 1
            )
            self.children.append(child_node)
    
    def rollout_policy(self, possible_moves):
        """
        Policy that defines the rollout strategy. Rollout is simulation.
        
        Classical Monte Carlo randomly selects a move from the possible
        moves to play and continues as such until the game is over.

        Can be updated with better policies.
        """
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def rollout(self):
        """
        From the current state, the rest of the game is simulated until completion and the outcome
        of the game is returned.

        Result is returned as 1-0 for white win, 0-1 for black win, and 1/2-1/2 for draw.
        """
        
        # create a board from the fen to use for the rollout
        rollout_board = chess.Board(fen=self.state)

        # while not current_rollout_state.is_game_over():
        count = 0
        while not rollout_board.is_game_over():
            # get all the legal moves from this position
            possible_moves = list(rollout_board.legal_moves)
            
            # select a move according to the rollout policy
            move = self.rollout_policy(possible_moves)

            # apply the move to the board
            # current_rollout_state = current_rollout_state.move(move)
            rollout_board.push(move)
            
            # increment the count
            count += 1
        
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
        # if the node has no children, expand it
        if self.children == []:
            self.expand()

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
    
    # choose the best move to take from
    def best_action(self):
        """
        Returns the node corresponding to the best possible move from a given state.

        This code calls expansion, simulation, and backpropagation.
        """

        simulation_no = 1000 # num simulations to run

        # expand the parent node
        self.expand()

        for i in range(simulation_no):

            # select a node from which to run the rollout
            v = self.best_child()

            # follow the node to the end of the game using the rollout policy
            reward = v.rollout()

            # backpropagate the result of the rollout through the tree
            v.backpropagate(reward)

        print(f"Number of visits: {self.number_of_visits}")
        return self.best_child().state
    
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
        Used to check if a node is terminal. Terminal node is when the game is over.
        """
        return self.board.is_game_over()
    
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
    best_next_state = MCTS_Node(
        state=state,
        color=color
    ).best_action()

    # TODO
    # compare the new state to the old state to get the move to return
    board = chess.Board(fen=state)
    move = ''
    moves = board.legal_moves

    # get the move that was made
    # TODO: can be optimized, leaving this for now
    for m in moves:
        board.push(m)
        if board.fen() == best_next_state:
            move = m
            break
        board.pop()

    return move

def main():
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

if __name__ == "__main__":
    start = time.time()
    main()
    # test_game()
    end = time.time()
    print(f"Time taken: {int(end - start)}s")