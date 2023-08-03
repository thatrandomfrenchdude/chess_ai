from entities.agent import Agent
from objects.board import Board
from ai.alphabeta import alphabeta
from config import ai_config

class Ai(Agent):
    def ai_move(self):
        # is this hardcoded to black?
        return self.get_ai_move(self.board, self.color, [])
    
    def move(self):
        print("AI is thinking...")
        while True:
            move = self.ai_move()
            valid = False
            possible_moves = self.board.get_possible_moves(self.color)
            # No possible moves
            if (move == 0 or not possible_moves):
                if move == 0:
                    print('move was 0')
                else:
                    print('no possible moves')
                return 0

            for possible_move in possible_moves:
                # got 0 here, which means line 42 did not work
                if (move.equals(possible_move)):
                    valid = True
                    break

            if (valid):
                break
            else:
                print("Invalid move.")
        return move

    # returns the best move for the ai to make
    @staticmethod
    def get_ai_move(chessboard, color, invalid_moves):
        best_move = 0
        best_score = ai_config.infinity
        for move in chessboard.get_possible_moves(color):
            if (Ai.is_invalid_move(move, invalid_moves)):
                continue

            copy = Board.clone(chessboard)
            copy.perform_move(move)

            score = alphabeta(copy, 2, -ai_config.infinity, ai_config.infinity, True, color)
            if (score < best_score):
                best_score = score
                best_move = move

        # Checkmate.
        if (best_move == 0):
            return 0

        copy = Board.clone(chessboard)
        copy.perform_move(best_move)
        if (copy.is_check(color)):
            invalid_moves.append(best_move)
            return Ai.get_ai_move(chessboard, color, invalid_moves)

        return best_move

    # returns whether a move is invalid or not
    # TODO: modify this to use caching instead of looping through all invalid moves
    @staticmethod
    def is_invalid_move(move, invalid_moves):
        for invalid_move in invalid_moves:
            if (invalid_move.equals(move)):
                return True
        return False