from entities.agent import Agent
from objects.move import Move

class User(Agent):
    # Returns a move object based on the users input.
    # Does not check if the move is valid.
    def get_user_move(self):
        print("Example Move: A2 A4")
        move_str = input("Your Move: ")
        move_str = move_str.replace(" ", "")

        try:
            xfrom = self.letter_to_xpos(move_str[0:1])
            yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
            xto = self.letter_to_xpos(move_str[2:3])
            yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
            return Move(xfrom, yfrom, xto, yto)
        except ValueError:
            print("Invalid format. Example: A2 A4")
            return self.get_user_move()

    # Returns a valid move based on the users input.
    def move(self):
        while True:
            valid = False
            
            # get user input
            move = self.get_user_move()

            possible_moves = self.board.get_possible_moves(self.color)
            # possible_moves = board.get_possible_moves(self.color)
            
            # No possible moves
            if (not possible_moves):
                return 0

            for possible_move in possible_moves:
                if (move.equals(possible_move)):
                    valid = True
                    break

            if (valid):
                break
            else:
                print("Invalid move.")
        return move
    
    # Converts a letter (A-H) to the x position on the chess board.
    def letter_to_xpos(self, letter):
        letter = letter.upper()
        if letter == 'A':
            return 0
        if letter == 'B':
            return 1
        if letter == 'C':
            return 2
        if letter == 'D':
            return 3
        if letter == 'E':
            return 4
        if letter == 'F':
            return 5
        if letter == 'G':
            return 6
        if letter == 'H':
            return 7

        raise ValueError("Invalid letter.")
    
    def xpos_to_letter(self, xpos):
        if xpos == 0:
            return 'A'
        if xpos == 1:
            return 'B'
        if xpos == 2:
            return 'C'
        if xpos == 3:
            return 'D'
        if xpos == 4:
            return 'E'
        if xpos == 5:
            return 'F'
        if xpos == 6:
            return 'G'
        if xpos == 7:
            return 'H'

        raise ValueError("Invalid xpos.")