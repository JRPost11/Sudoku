from timing import *

# This module is used to test the program using some test puzzles defined in test_puzzles.txt.

def process_txt():
    lines = []

    # Open the file and append certain lines to a list
    file = open("test_puzzles.txt")
    for i, line in enumerate(file):
        if 6 <= i:
            lines.append(line)

    file.close()

    board_list = []

    # Go through every line and split it into a board, its number of solutions and, if possible, its solution.
    for line in lines:
        lists = line.split(":")

        board = []
        n_solutions = []
        solved_board = []
        i = 0

        for list in lists:
            match i:
                case 0:
                    for character in list:
                        if character == ".":
                            board.append(0)
                        else:
                            board.append(int(character))
                case 1:
                    n_solutions = int(list.replace("\n", ""))
                case 2:
                    for character in list:
                        if character == "\n":
                            continue
                        else:
                            solved_board.append(int(character))

            i += 1

        board_list.append([board, n_solutions, solved_board])

    return board_list


def testing_puzzles():
    # Process the text file to extract boards
    board_list = process_txt()

    # Solve every board and record how long it takes.
    for i in range(43):
        time_solver(board_list[i][0], i, "multiple")

