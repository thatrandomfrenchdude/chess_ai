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
from collections import defaultdict

class MCTS_Node:
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        return
    
    def untried_actions(self):
        """
        Returns the list of untried actions from a given state
        """
        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions
    
    def q(self):
        """
        Returns the difference between wins and losses
        """
        wins = self._results[1]
        losses = self._results[-1]
        return wins - losses
    
    def n(self):
        """
        return the number of times the current node has been visited
        """
        return self._number_of_visits

    def expand(self):
        """
        From the given state, the next state is generated depending on the action.

        In this step, all possible child nodes of the generated state are appended to the
        children array and the child node is returned.

        Thethe states which are possible from the present state are all generated and the child node
        corresponding to the generated state is returned.
        """
        action = self._untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MCTS_Node(
            next_state,
            parent=self,
            parent_action=action
        )
        self.children.append(child_node)
        return child_node
    
    def is_terminal_node(self):
        """
        Used to check if a node is terminal. Terminal node is when the game is over.
        """
        return self.state.is_game_over()
    
    def rollout(self):
        """
        From the current state, the rest of the game is simulated until completion and the outcome
        of the game is returned.

        For wins, 1 is returned.
        For losses, -1 is returned.
        For draws, 0 or 0.5 is returned. 0.5 can be used when a draw is preferable to a loss.
        """
        current_rollout_state = self.state

        while not current_rollout_state.is_game_over():
            possible_moves = current_rollout_state.get_legal_actions()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result()
    
    def backpropagate(self, result):
        """
        All node statistics are updated until the parent node is reached.

        win/draw/loss results and node visits are incremented.
        """
        self._number_of_visits += 1
        self._results[result] += 1  # assumes result is the key for the results dict. 0.5 won't work
        if self.parent:
            self.parent.backpropagate(result)

    def is_full_expanded(self):
        """
        Checks if all possible actions from a given node have been tried.
        """
        return len(self._untried_actions) == 0
    
    def best_child(self, c_param=0.1):
        """
        After the tree is fully expanded, the best child is selected based on the upper confidence bound.

        The first term in the equation is the exploitation.
        The second term in the equation is the exploration.
        """
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    def rollout_policy(self, possible_moves):
        """
        Randomly selects a move from the possible moves.

        Can (and should) be updated with better policies.
        """
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def _tree_policy(self):
        """
        Selects the node on which to run rollout
        """
        current_node = self
        while not current_node.is_terminal_node():
            if not current_node.is_full_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node
    
    def best_action(self):
        """
        Returns the node corresponding to the best possible move from a given state.

        This code calls expansion, simulation, and backpropagation.
        """
        simulation_no = 100 # num simulations to run

        for i in range(simulation_no):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)

        return self.best_child(c_param=0)
    
    def get_legal_actions(self) -> list:
        """
        Should return all legal moves from a given positon.

        Modify for the use case.
        """
        return []
    
    def is_game_over(self) -> bool:
        """
        Determines whether a game is over.

        Modify for the use case.
        """
        return True
    
    def game_result(self):
        """
        Returns the final game results.

        Modify according to the use case.

        For wins, 1 is returned.
        For losses, -1 is returned.
        For draws, 0 or 0.5 is returned. 0.5 can be used when a draw is preferable to a loss.
        """
        return 0
    
    def move(self, action):
        """
        Apply a move to the game and change the state.

        Modify according to the use case.

        Returns the new state after the move is applied.
        """
        pass

def main():
    """
    Returns the best move from a given position.
    """
    initial_state = []  # modify according to the use case
    root = MCTS_Node(state=initial_state)
    selected_node = root.best_action()
    return