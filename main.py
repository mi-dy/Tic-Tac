from board import Board

def main():
    board = Board()
    board.draw()
    while True:
        board.place_x(int(input("Where to mark? Coordinate x: ")), int(input("Where to mark? Coordinate y: ")))
        board.draw()
        board.check_victory(board)

if __name__ == "__main__":
    main()