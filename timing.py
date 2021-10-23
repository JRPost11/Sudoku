import time

from solver import *
from utility import check_board


# Calculates time taken to solve a board
def time_solver(board: list, number: int, debug=False):
    start = time.time()
    solvable, solved_board, n = solver(board)

    if len(n) == 1:
        solvable = 1
    else:
        solvable = 0

    print(f"Number of solutions: {len(n)}")
    print(f"Board {number} solvable: {solvable}")
    end = time.time()
    print(f"Time taken to solve board {number}: {end - start}\n")


# Calculates time taken to check board
def time_checker(board: list, number: int):
    start = time.time()
    print(f"Board {number} legal: {check_board(board)}")
    end = time.time()
    print(f"Time taken to check board {number}: {end - start}")
