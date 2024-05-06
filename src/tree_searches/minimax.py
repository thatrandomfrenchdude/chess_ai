import math
from evaluate import evaluate

# references
# https://philippmuens.com/minimax-and-mcts

# w = tree width, the approximate number of child nodes each node will have
# d = depth, where each layer represents on move in the game
# w^d is the average number of different positions to evaluate

##### improved alpha beta minimax algorithm #####
# checks only states in the tree that are better than the best
def alpha_beta_minimax(state, max_depth, is_player_minimizer, alpha, beta):
    if max_depth == 0 or state.is_end_state():
        # We're at the end. Time to evaluate the state we're in
        return evaluate(state)

    return ab_minimizer(state, max_depth, alpha, beta) if is_player_minimizer \
        else ab_maximizer(state, max_depth, alpha, beta)

def ab_minimizer(state, max_depth, alpha, beta):
    value = -math.inf
    for move in state.possible_moves():
        evaluation = alpha_beta_minimax(move, max_depth - 1, False, alpha , beta)
        min = min(value, evaluation)
        # Keeping track of our current best score
        beta = min(beta, evaluation)
        if beta <= alpha:
            break
    return value

def ab_maximizer(state, max_depth, alpha, beta):
    value = math.inf
    for move in state.possible_moves():
        evaluation = alpha_beta_minimax(move, max_depth - 1, True, alpha, beta)
        max = max(value, evaluation)
        # Keeping track of our current best score
        alpha = max(alpha, evaluation)
        if beta <= alpha:
            break
    return value

##### standard minimax algorithm #####
# checks all states in a game tree
def minimax(state, max_depth, is_player_minimizer):
    if max_depth == 0 or state.is_end_state():
        # We're at the end. Time to evaluate the state we're in
        return evaluate(state)

    # Is the current player the minimizer?
    return minimizer(state, max_depth) if is_player_minimizer \
        else maximizer(state, max_depth)

def maximizer(state, max_depth):
    value = -math.inf
    for move in state.possible_moves():
        evaluation = minimax(move, max_depth - 1, False)
        min = min(value, evaluation)
    return value

def minimizer(state, max_depth):
    value = -math.inf
    for move in state.possible_moves():
        evaluation = minimax(move, max_depth - 1, False)
        min = min(value, evaluation)
    return value