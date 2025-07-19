import sys

class Board:
    def __init__(self, ln1=["", "", ""], ln2=["", "", ""], ln3=["", "", ""]):
        self.ln1 = ln1
        self.ln2 = ln2
        self.ln3 = ln3

    def draw(self):
        print(f"{self.sq1}|{self.sq2}|{self.sq3}\n-----\n{self.sq4}|{self.sq5}|{self.sq6}\n-----\n{self.sq7}|{self.sq8}|{self.sq9}")

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

