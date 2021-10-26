import time

from solver import *
from utility import check_board


# Calculates time taken to solve a board
def time_solver(board: list, number: int, mode: str):
    start = time.time()

    # Solving the board and recording using information
    solvable, solved_board, n_solutions = solver_control(board, mode)

    # Prints useful information like, solvability, number of solutions, and if there is a unique solution, it prints
    # the solution. It also prints the time taken to solve the board.
    print_board(board)
    print(f"Board {number} solvable: {solvable}")
    print(f"Number of solutions: {n_solutions}")

    if n_solutions == 1:
        print(f"Solution of board {number}:")
        print_board(solved_board)

    end = time.time()

    print(f"Time taken to solve board {number}: {end - start}\n")


# Calculates time taken to check board
def time_checker(board: list, number: int):
    start = time.time()
    print(f"Board {number} legal: {check_board(board)}")
    end = time.time()
    print(f"Time taken to check board {number}: {end - start}")
