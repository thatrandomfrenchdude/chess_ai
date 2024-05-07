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
        self.color = board.turn # the color of the player
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
            "win": 0, # wins
            "draw": 0, # draws
            "loss": 0 # losses
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
        start_fen = self.board.fen()

        # while not current_rollout_state.is_game_over():
        count = 0
        while not self.board.is_game_over():
            # get all the legal moves from this position
            possible_moves = self.board.get_legal_actions()
            
            # select a move according to the rollout policy
            move = self.rollout_policy(possible_moves)

            # apply the move to the board
            # current_rollout_state = current_rollout_state.move(move)
            self.board.push(move)
            
            # increment the count
            count += 1
        
        # get the game result
        outcome = self.board.outcome()
        result = outcome.result()

        # undo the moves
        for _ in range(count):
            self.board.pop()

        # confirm matching fen
        assert start_fen == self.board.fen()

        # interpret the result and return it
        return result
    
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

def test_game():
    game = chess.Board(fen='rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1')
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
    # main()
    test_game()