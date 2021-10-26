from generator import *
from testing import *


def main():
    # testing_puzzles()
    board, cells_left = generate_board(difficulty="easy")
    print(f"Number of cells left: {cells_left}")

    time_solver(board, 1, "multiple")


if __name__ == '__main__':
    main()
