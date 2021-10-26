from utility import *

global solved_board, n_solutions


# Function that controls the solving of a board
def solver_control(board: list, mode: str):
    # Create a copy of the given board, since the given board should not be changed.
    board_copy = board.copy()
    # Check if the given board is legal.
    if check_board(board) is not True:
        raise ValueError("Given board is not legal.")

    global solved_board, n_solutions
    solved_board = []
    n_solutions = 0

    # Depending on the mode, it calls different solver functions.
    # Mode 'single' is used when it is known that a sudoku has a unique solution.
    if mode == "single":
        solvable = solver_single_solution(board_copy)

        return solvable, solved_board, n_solutions

    # Mode 'multiple' is used when the number of solutions is not known and a board's legality needs to be checked.
    elif mode == "multiple":
        solvable = solver_multiple_solutions(board_copy)

        return solvable, solved_board, n_solutions

    # If the mode is not defined, an error is raised.
    else:
        raise ValueError("Mode has not been assigned properly!")


# Solves a sudoku. Does not check how many solutions there are. Should only be used for sudoku's where it is known that
# there is just one solution
def solver_single_solution(board: list):
    global solved_board, n_solutions

    # Find an empty cell on the given board
    index = find_empty_cell(board)

    # If there are no empty cells left, record the current board and increase the number of solutions
    if not index:
        solved_board.append(board)
        n_solutions += 1

        return True

    # Loop through each possible value for the current cell
    for i in range(1, 10):
        # Check if the given value is possible, if it's not continue to the next value. If it is, assign the value
        # to the cell and recursively continue.
        if check_cell(board, i, index):
            board[index] = i

            # Check recursively if the current board layout is correct, if it is return True.
            if solver_single_solution(board):
                return True

            # Current board layout does not work out, so reverse the assignment of the value to the cell.
            board[index] = 0

    # If none of the values work for a given cell, the current board layout is wrong.
    return False


# Solver which can determine if a sudoku has multiple solutions. Used by the sudoku generation function.
def solver_multiple_solutions(board: list):
    global solved_board, n_solutions

    index = find_empty_cell(board)

    # If there are no empty cells left, save the board and increase the number of solutions
    if index is None:
        solved_board += board
        n_solutions += 1
        return True

    # Loop through the possible values for the cell
    for number in range(1, 10):
        # Check if the board is still legal with the given value for the cell. If it is not, try another value. If it is
        # set the cell to that value.
        if check_cell(board, number, index):
            board[index] = number

            # Continue recursively until a solution has been found.
            if solver_multiple_solutions(board):
                board[index] = 0
            else:
                return False

    return True
