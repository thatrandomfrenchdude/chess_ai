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

# TODO:
# want to make this recursive with stopping conditions I think
# implement a sql database w/ api to store transposition table

class MCTS_Node:
    def __init__(self, board, parent=None, max_depth=3):
        # node
        self.board = board # the current state of the game
        self.state = self.board.fen() # the current state of the game
        self.max_depth = max_depth # the maximum depth of the tree
        
        # relatives
        self.parent: MCTS_Node | None = parent # the parent state of the current state
        # self.parent_action: str = parent_action
        self.children: list[MCTS_Node] = [] # children of the current node

        # the number of times the current node has been visited
        self.number_of_visits = 0
        
        # stores the record of the current node as the sum of all subsequent nodes
        self.results = {
            "wins": 0,
            "draws": 0,
            "losses": 0
        }

        if max_depth > 0:
            self.expand()

    def expand(self):
        """
        From the given state, the next state is generated depending on the action.

        In this step, all possible child nodes of the generated state are appended to the
        children array and the child node is returned.

        The states which are possible from the present state are all generated and the child node
        corresponding to the generated state is returned.
        """
        # apply the action to the node
        # action = self.legal_moves.pop()
        # next_state = self.state.move(action)
        for move in self.board.legal_moves:
            # generate a new board --> 56 bytes
            child_board = chess.Board(fen=self.state)
            
            # apply the move to the board
            child_board.push(move)

            # create a new node, passing the board and the parent node
            child_node = MCTS_Node(
                child_board,
                parent=self,
                max_depth=self.max_depth - 1
            )
            self.children.append(child_node)
    
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
    
    def backpropagate(self, result) -> None:
        """
        All node statistics are updated until the parent node is reached.

        win/draw/loss results and node visits are incremented.
        """
        self.number_of_visits += 1

        if result == 1:
            self.results["wins"] += result
        elif result == 0.5:
            self.results["draw"] += result
        else: # -1
            self.results["losses"] += result

        # if the node has a parent, pass up the result
        if self.parent:
            self.parent.backpropagate(result)
    
    def best_child(self, temp=0):
        """
        Choose the best child is based on the upper confidence bound.

        The first term in the equation is the exploitation, the second
        is the exploration.
        """
        def exploit(child: MCTS_Node):
            return child.get_win_loss() / child.get_num_visits()
        
        def explore(child: MCTS_Node):
            return temp * np.sqrt((2 * np.log(self.get_num_visits()) / child.get_num_visits()))
        
        # calculate the ucb for each child
        ucbs = [exploit(child) + explore(child) for child in self.children]
        
        # return the child with the highest ucb
        return self.children[np.argmax(ucbs)]
    
    def rollout_policy(self, possible_moves):
        """
        Policy that defines the rollout strategy. Rollout is simulation.
        
        Classical Monte Carlo randomly selects a move from the possible
        moves to play and continues as such until the game is over.

        Can be updated with better policies.
        """
        return possible_moves[np.random.randint(len(possible_moves))]
    
    # def tree_policy(self):
    #     """
    #     Selects the node on which to run rollout

    #     Select the best child of the current node based on the UCB1 formula.

    #     Assumes the tree has been expanded to the max depth
    #     """
    #     return self.best_child() # \
    #     #     if (self.children and not self.is_terminal_node()) \
    #     #         else self
    
    # choose the best move to take from
    def best_action(self):
        """
        Returns the node corresponding to the best possible move from a given state.

        This code calls expansion, simulation, and backpropagation.
        """
        simulation_no = 100 # num simulations to run

        for i in range(simulation_no):
            # select a node from which to run the rollout
            # v = self.tree_policy()
            v = self.best_child()

            # follow the node to the end of the game using random moves
            reward = v.rollout()

            # backpropagate the result of the rollout through the tree
            v.backpropagate(reward)

        return self.best_child(c_param=0)
    
    def is_terminal_node(self):
        """
        Used to check if a node is terminal. Terminal node is when the game is over.
        """
        return self.board.is_game_over()
    
    # was q
    def get_win_loss(self):
        """
        Returns the difference between wins and losses
        """
        return self.results["wins"] - self.results["loses"]
    
    # was n
    def get_num_visits(self):
        """
        return the number of times the current node has been visited
        """
        return self.number_of_visits
    
    def game_result(self):
        """
        Returns the final game results.

        Modify according to the use case.

        For wins, 1 is returned.
        For losses, -1 is returned.
        For draws, 0 or 0.5 is returned. 0.5 can be used when a draw is preferable to a loss.
        """
        return 0

def best_move(state, engine):
    """
    Returns the best move from a given state.
    """
    # run a monte carlo tree search on a given state
    new_state = MCTS_Node(engine, state=state).best_action()
    return new_state.move() # the state needs to contain the move taken. '' for start

def main():
    """
    Returns the best move from a given position.
    """
    initial_state = []  # modify according to the use case
    # define a base state, choose the next best state
    # root = MCTS_Node(state=initial_state)
    # selected_node = root.best_action()

    # modify this to choose the next best state given a state.
    class Engine:
        def __init__(self, initial_state=None):
            self.board = chess.Board() if not initial_state else chess.Board(fen=initial_state)
            self.size = sys.getsizeof(self.board)

    board_engine = Engine()
    print(f"size of engine: {sys.getsizeof(board_engine)}")
    print(board_engine.board)
    board_engine.board.push(np.random.choice(list(board_engine.board.legal_moves)))
    print(board_engine.board)
    sys.exit()

    game = 1 # define a chess game
    state = 1 # initial chess state
    return best_move(state, engine)

if __name__ == "__main__":
    main()