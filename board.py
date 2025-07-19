import sys

class Board:
    def __init__(self, ln1=[" ", " ", " "], ln2=[" ", " ", " "], ln3=[" ", " ", " "]):
        self.ln1 = ln1
        self.ln2 = ln2
        self.ln3 = ln3

    def draw(self):
        i = 0
        for line in [self.ln1, self.ln2, self.ln3]:
            print("|".join(item for item in line))
            if i <= 1:
                print("------")
                i += 1

    def place_x(self, position):
        setattr(self, position, "x")

    def place_o(self, position):
        setattr(self, position, "o")

    def check_victory(self, board):

        for line in board:
            if all(item == "x" for item in line):
                sys.exit("Vicotry royal!")
            elif all(item == "o" for item in line):
                sys.exit("Loser!")
        
        column = []
        i = 0
        for line in board:
            column.append(line[i])
        if all(item == "x" for item in column):
            sys.exit("Vicotry royal!")
        elif all(item == "o" for item in column):
            sys.exit("Loser!")
        
        diagonal = []
        j = 0
        for line in board:
            diagonal.append(line[j])
            j += 1

