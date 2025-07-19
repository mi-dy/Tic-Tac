import sys
from board import Board

class Line(Board):
    def __init__(self, sq1, sq2, sq3):
        super().__init__(sq1, sq2, sq3)

    def check(self):
        if self.sq1 == self.sq2 == self.sq3 == "x":
            sys.exit("Victory royal!")
        elif self.sq1 == self.sq2 == self.sq3 == "o":
            sys.exit("Loser!")