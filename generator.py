import random

from utility import *
from solver import solver


# Function called to generate a board depending on the given difficulty
def generate_board(difficulty="normal"):
    board = [0 for x in range(81)]

    # Generate a full board
    generate_full_board(board, 0)

    # In case the generate full board is illegal, a value error is raised
    if not check_board(board):
        raise ValueError("Generated full board is not legal")

    # Deciding the minimum amount of cells left, depending on the difficulty
    match difficulty:
        case "easy":
            min_cells_left = 25
        case "normal":
            min_cells_left = 21
        case "hard":
            min_cells_left = 17
        case _:
            raise ValueError("Difficulty argument has not been assigned a proper value")

    # Removes cells until the amount of cells left reaches a given minimum
    remove_cells(board, min_cells_left)

    return board


# Function that generates a random full board
def generate_full_board(board: list, index: int):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)

    numbers_index = 0

    while numbers_index <= 8:
        # If the board is full and legal, break out of the loop
        if check_board(board) and board[80] != 0:
            break

        # Assign a random value to the index
        board[index] = numbers[numbers_index]

        # Check if the board is legal, if it is, go the the next index. If it's not try another random number.
        if check_board(board):
            # Checking if next index returns a legal board, if it does, the function reached the last index and
            # generated a legal board. If not, the value assigned to the index does not result in a legal board.
            if generate_full_board(board, index + 1):
                break
            else:
                numbers_index += 1
        else:
            numbers_index += 1

        # If all 9 numbers have been tried, and no legal board has resulted from it. Reset the current index, and
        # return false.
        if numbers_index > 8:
            board[index] = 0
            return False

    return True


def remove_cells(board: list, min_cells_left: int):
    cells_left = 81
    index = 0
    index_list = [x for x in range(81)]

    random.shuffle(index_list)

    while check_board(board) and cells_left > min_cells_left:
        last_value = board[index_list[index]]
        board[index_list[index]] = 0

        # print(f"Index: {index}, index_list: {index_list[index]}")
        # print(f"Cells left: {cells_left - 1}")
        # print_board(board)

        # print("")

        if cells_left < 30:
            solvable, solved_board = solver(board)
        else:
            solvable = True

        if solvable:
            cells_left -= 1
            index += 1
            continue
        else:
            board[index_list[index]] = last_value
            return board
