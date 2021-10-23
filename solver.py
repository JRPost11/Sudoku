from utility import *


# Function that solves a given board
def solver(board: list):
    # Create a copy of the given board, since the given board should not be changed.
    solved_board = board.copy()
    # Check if the given board is legal.
    if check_board(board) is not True:
        raise ValueError("Given board is not legal.")

    return solver_help(solved_board), solved_board


def solver_help(board: list):
    index = find_empty_cell(board)

    if not index:
        return True

    for i in range(1, 10):
        if check_cell(board, i, index):
            board[index] = i

            if solver_help(board):
                return True

            board[index] = 0

    return False


# Recursive function that helps to solve the board, much slower than other function
# def solver_help(board: list, index: int):
#     value = 1
#
#     # If current index is empty, assign it a value. If not, go to next index.
#     if board[index] == 0:
#         while True:
#             # Assign the index a value
#             board[index] = value
#
#             # Check if the board is still legal
#             if check_board(board):
#                 # If the final index has been reached, return that the board is solved and legal. Else try the next
#                 # index, if that does not return true, the current value for this index does not result in a legal
#                 # board. So increases the current value of this square.
#                 if index == 80:
#                     return True
#                 elif solver_help(board, index + 1):
#                     return True
#                 else:
#                     value += 1
#             else:
#                 # Board is not legal, try increasing the value at current index
#                 value += 1
#
#                 # Value reaches a maximum, means a legal full board can't be gotten with current board configuration.
#                 # Reset value at current index, and return false.
#                 if value > 9:
#                     board[index] = 0
#                     return False
#     else:
#         # If last index has been reached, return true. Else continue with the next index.
#         if index < 80:
#             return solver_help(board, index + 1)
#         else:
#             return True



