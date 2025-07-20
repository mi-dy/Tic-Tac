import sys

class Board:
    def __init__(self):
        self.board = [[" ", " ", " "]for _ in range(3)]


    def __getitem__(self, coord):
        return self.board[coord]


    def draw(self):
        i = 0
        for line in self.board:
            print("|".join(item for item in line))
            if i <= 1:
                print("------")
                i += 1


    def place_x(self, x, y):
        self.board[x][y] = "x"


    def place_o(self, x, y):
        self.board[x][y] = "o"


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


        return None
