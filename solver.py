from utility import *


# Function that solves a given board
def solver(board: list):
    # Create a copy of the given board, since the given board should not be changed.
    board_copy = board.copy()
    # Check if the given board is legal.
    if check_board(board) is not True:
        raise ValueError("Given board is not legal.")

    solved_board = []
    number_of_solutions = []

    # return solver_help(solved_board, number_of_solutions), solved_board, number_of_solutions
    # return solver_help2(board_copy, solved_board, number_of_solutions), solved_board
    return solver_help3(board_copy, solved_board, number_of_solutions), solved_board, number_of_solutions


# Solves sudoku. Does not check how many solutions there are. Should only be used for sudoku's where it is known that
# there is just one solution
def solver_help(board: list, n: list):
    index = find_empty_cell(board)

    if not index:
        n.append('solution')
        return True

    for i in range(1, 10):
        if check_cell(board, i, index):
            board[index] = i

            if solver_help(board, n):
                return True

            board[index] = 0

    return False


def solver_help3(board: list, solved_board: list, number_of_solutions: list):
    index = find_empty_cell(board)
    # print(f"Index: {index}")

    if not index:
        # print("Found solution")
        solved_board.append(board)
        number_of_solutions.append(0)
        return 1

    if len(number_of_solutions) > 1:
        return -1

    for number in range(1, 10):
        if check_cell(board, number, index):
            # print(f"Number: {number}")
            board[index] = number

            solved = solver_help3(board, solved_board, number_of_solutions)

            if solved == 0 or solved == 1:
                board[index] = 0
            else:
                return -1
                # print("Returned, board value not good")
            # elif solved == 1:
            #     board[index] = 0
            # print("Returned, board solved. Trying to find another solution.")

    return 0
