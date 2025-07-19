import sys

class Board:
    def __init__(self, sq1=" ", sq2=" ", sq3=" ", sq4=" ", sq5=" ", sq6=" ", sq7=" ", sq8=" ", sq9=" "):
        self.sq1 = sq1
        self.sq2 = sq2
        self.sq3 = sq3
        self.sq4 = sq4
        self.sq5 = sq5
        self.sq6 = sq6
        self.sq7 = sq7
        self.sq8 = sq8
        self.sq9 = sq9
    
    def draw(self):
        print(f"{self.sq1}|{self.sq2}|{self.sq3}\n-----\n{self.sq4}|{self.sq5}|{self.sq6}\n-----\n{self.sq7}|{self.sq8}|{self.sq9}")

    def place_x(self, position):
        setattr(self, position, "x")

    def place_o(self, position):
        setattr(self, position, "o")
