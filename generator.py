import random

from solver import *

global cells_left


# Function called to generate a board depending on the given difficulty
def generate_board(difficulty="normal"):
    global cells_left

    board = [0 for x in range(81)]
    cells_left = 81

    # Generate a full board
    generate_full_board(board, 0)

    # In case the generated full board is illegal, a value error is raised
    if not check_board(board):
        raise ValueError("Generated full board is not legal")

    # Deciding the minimum amount of cells left, depending on the difficulty
    match difficulty:
        case "easy":
            min_cells_left = 40
        case "normal":
            min_cells_left = 21
        case "hard":
            min_cells_left = 17
        case _:
            raise ValueError("Difficulty argument has not been assigned a proper value")

    count = 0
    # Removes cells until the amount of cells left reaches a given value
    while True:
        count += 1
        print(count)
        board_try = board.copy()
        remove_cells(board, min_cells_left)

        print(f"Cells left: {cells_left}. Minimum cells left: {min_cells_left}")
        if cells_left == min_cells_left:
            break

        board = board_try

    return board, cells_left


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

        # Check if the board is legal and if the next index returns a legal board. If both are true, break from the
        # loop, else try another random value at the index.
        if check_board(board) and generate_full_board(board, index + 1):
            break
        else:
            numbers_index += 1

        # If all 9 numbers have been tried, and no legal board has resulted from it. Reset the current index, and
        # return false.
        if numbers_index > 8:
            board[index] = 0
            return False

    return True


# Function that removes cells until a certain amount of cells left has been reached. Makes sure that board is still
# legal.
def remove_cells(board: list, min_cells_left: int):
    global cells_left

    cells_left = 81
    index = 0

    # Creates a list of all the indux numbers and shuffles it
    index_list = [x for x in range(81)]
    random.shuffle(index_list)

    while check_board(board):
        # Store the last value at the index, if the new board is found to be illegal.
        last_value = board[index_list[index]]

        # Making a hole at a certain index
        board[index_list[index]] = 0

        # Solving the board
        solvable, solved_board, n_solutions = solver_control(board, "multiple")

        # Checking if the board is solvable and has a unique solution. If it is not, reset the value at the current
        # index and return the board
        if solvable and n_solutions == 1:
            cells_left -= 1
            index += 1

            # If a certain amount of cells have been emptied, return the board
            if cells_left == min_cells_left:
                return board
        else:
            board[index_list[index]] = last_value
            return board
