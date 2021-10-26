# Prints the 9 x 9 board to the command line
def print_board(board: list):
    for row in range(9):
        for column in range(9):
            print(f"{board[column + row * 9]} " if (column + 1) % 3 != 0 else f"{board[column + row * 9]} \t", end="")
        print(f"" if (row + 1) % 3 != 0 else f"\n")


# Finds the first empty cell on the board by looping through the whole board
def find_empty_cell(board: list):
    for index in range(81):
        if board[index] == 0:
            return index


# Checks if the board configuration is legal
def check_board(board: list):
    for index in range(81):
        # Checking for an edge case where a value is higher than 9, which is illegal
        if board[index] > 9:
            return False

        # Checking rows
        row = index // 9

        for column in range(0, 9):
            if index != column + row * 9 and board[index] == board[column + row * 9] and board[index] != 0:
                return False

        # Checking columns
        column = index % 9

        for row in range(0, 9):
            if index != column + row * 9 and board[index] == board[column + row * 9] and board[index] != 0:
                return False

        # Check 3 x 3
        # First calculates the top left coordinates of the 3 x 3 the square is in
        row_tl = index // 9 // 3 * 3
        column_tl = index % 9 // 3 * 3

        # Checks the rest of the 3 x 3 if there is a duplicate value
        for row in range(row_tl, row_tl + 3):
            for column in range(column_tl, column_tl + 3):
                if index != column + row * 9 and board[index] == board[column + row * 9] and board[index] != 0:
                    return False

    return True


# Checks if the board is still legal given an additional number at a certain index
def check_cell(board: list, number: int, index: int):
    # Check row
    row = index // 9

    for column in range(9):
        if index != column + row * 9 and board[column + row * 9] == number:
            return False

    # Check column
    column = index % 9

    for row in range(9):
        if index != column + row * 9 and board[column + row * 9] == number:
            return False

    # Check 3 x 3
    row_tl = index // 9 // 3 * 3
    column_tl = index % 9 // 3 * 3

    for row in range(row_tl, row_tl + 3):
        for column in range(column_tl, column_tl + 3):
            if index != column + row * 9 and board[column + row * 9] == number:
                return False

    return True
