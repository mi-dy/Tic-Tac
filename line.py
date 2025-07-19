import sys

class Line():
    def __init__(self, line):
        self.line = line

    def check(self, line):
        if all[line] == "x":
            sys.exit("Wictory royal!")
        elif all[line] == "o":
            sys.exit("Loser!")