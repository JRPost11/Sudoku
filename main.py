import time

from board import *
from generator import *
from solver import *
from timing import *
from utility import *


def main():
    # board = generate_board()
    #
    # print_board(board)

    # start_total = time.time()
    # n = 0
    # board_list = []
    #
    # for i in range(10):
    #     s = time.time()
    #     board = generate_board(difficulty="easy")
    #     solver(board)
    #     e = time.time()
    #
    #     if e - s > 1:
    #         board_list.append(board)
    #         n += 1
    #
    #     print(f"Time taken to generate and solve board {i}: {e - s}")
    #
    # end_total = time.time()
    # print(f"Time taken to generate and solve 100 boards: {end_total - start_total}")
    #
    # print(f"The following {n} boards took longer than 1 second to solve.")
    # for index in range(len(board_list)):
    #     print(f"Board {index}")
    #     print_board(board_list[index])

    # time_solver(board1, 1)
    # time_solver(board2, 2)
    # time_solver(board3, 3)

    time_solver(board1, 1)
    time_solver(board2, 2)
    time_solver(board3, 3)
    time_solver(board4, 4)


if __name__ == '__main__':
    main()
