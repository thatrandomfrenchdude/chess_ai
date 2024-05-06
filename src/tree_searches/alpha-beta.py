import math
from evaluate import evaluate

### Max vs Min ###
# NOTE
# Making and unmaking moves is omitted,
# and should be done before and after
# the recursive calls

def alphaBetaMax(alpha: int, beta: int, depthleft: int) -> int:
    if depthleft == 0:
        return evaluate()
    
    # generate a list of moves
    moves = []
    
    # evaluate moves
    for move in moves:
        # make the move
        score = alphaBetaMin(alpha, beta,depthleft - 1)
        # take back the move
      
        # fail hard beta-cutoff
        if score >= beta:
            return beta
      
        # alpha acts like max in MiniMax
        if score > alpha:
            alpha = score
    return alpha

def alphaBetaMin(alpha: int, beta: int, depthleft: int) -> int:
    if depthleft == 0:
        return -evaluate()
    
    # generate a list of moves
    moves = []

    for move in moves:
        # make the move
        score = alphaBetaMax(alpha, beta, depthleft - 1)
        # take back the move

        # fail hard alpha-cutoff
        if score <= alpha:
            return alpha
        # beta acts like min in MiniMax
        if score < beta:
            beta = score
    return beta

depth = 10
score = alphaBetaMax(-math.inf, math.inf, depth)

# Negamax

def quiesce(alpha: int, beta: int) -> int:
    """
    quiesence searce
    
    https://www.chessprogramming.org/Quiescence_Search
    """
    stand_pat: int = evaluate()
    
    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    # generate list of captures
    captures = []

    for capture in captures:
        # make the capture
        score = -quiesce(-beta, -alpha)
        # take back the move

        if score >= beta:
            return beta
        if score > alpha:
            alpha = score
    
    return alpha