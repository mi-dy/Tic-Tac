import sys

class Line():
    def __init__(self, line):
        self.line = line

    def check_victory(self, line):
        if all(item == "x" for item in line):
            sys.exit("Victory royal!")
        elif all(item == "o" for item in line):
            sys.exit("Loser!")
        return None