from evaluate import evaluate

# references
# https://philippmuens.com/minimax-and-mcts

temperature = 1.5

class Node:
    def __init__(self, state, parent):
        self.t = 0 # total score of the node, or, how many times total the node has been traversed
        self.n = 0 # number of times the node has been visited

        self.game_state = state

        # relatives
        self.parent = parent
        self.children = []

def upper_confidence_bound(
    xi: int, # t value of current node
    c: float, # temperature --> exploitation (depth) vs exploration (breadth)
    N: int, # number of visits to the parent node
    n: int # number of visits to the current node
):
    # xi + c * sqrt(log(N)/ni)
    import numpy as np

    # very small number to prevent division by 0
    very_small_value = 1/(-10**10)

    ucb = xi + c * np.sqrt(np.log(N)/(n+very_small_value))
    return ucb

# save visited game states
transposition_table = {}

def get_legal_moves(state) -> list:
        """
        Should return all legal moves from a given positon.

        Modify for the use case.
        """
        return []

# applies a move to a state to get the next state
def get_new_state(state, move):
    new_state = []
    return new_state

# run simulations and return a score
def rollout(state) -> int:
    return 0

# perform a monte carlo tree search for a state, returning the best choice for next state
def MCTS(
    state, # current game state
    iterations: int = 100,
) -> int:
    # create the root node from the current state
    root = Node(state, None)

    # calculate all possible moves for this state
    possible_moves = get_legal_moves(state)

    # use possible moves to generate the child nodes
    # expand
    children = [Node(get_new_state(state, move), root) for move in possible_moves]

    for _ in range(iterations):
         # calculate the ucb for each child --> breadth first
        ucbs = [upper_confidence_bound(node.t, temperature, root.t, node.n) for node in children]

        # pick the node to visit by highest ucb of all children
        node_to_visit = children[ucbs.index(max(ucbs))]

        # perform rollout on the selected node and update t and n
        node_to_visit.t = rollout(node_to_visit.state)
        node_to_visit.n += 1

    # calculate the ucbs once more
    ucbs = [upper_confidence_bound(node.t, temperature, root.t, node.n) for node in children]

    # return the next node to visit
    return children[ucbs.index(max(ucbs))]
    


        

