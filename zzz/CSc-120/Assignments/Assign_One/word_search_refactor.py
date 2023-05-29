# Word Search Refactor
# Author: Anthony Bosek
# Date: 5/29/23
#
# Description: This program will take a grid of letters and a list of words and find the words in the grid.
#              Words can be found horizontally, vertically, and diagonally.
#              Words should be printed to console one per line in alphabetical order.


# function to create word list from supplied input file
def create_word_list(filename):
    word_list = []
    allWords = open(filename)
    for word in allWords:
        word_list.append(word.strip())
    allWords.close()
    return word_list


# function to create grid from supplied input file
def create_grid(filename):
    grid = []
    sampleGrid = open(filename)
    for line in sampleGrid:
        line = line.split()
        grid.append(line)
    sampleGrid.close()
    return grid


# function to modify original grid into new rows of origional columns
def create_column_grid(input_grid):
    column_grid = []
    for i in range(len(input_grid)):
        column = []
        for j in range(len(input_grid[i])):
            column.append(input_grid[j][i])
        column_grid.append(column)
    return column_grid


# function to modify original grid into new rows of diagonal columns
def create_diagonal_grid(input_grid):
    diagonal_grid = []
    for row in range(len(input_grid)):
        for offset in range(len(input_grid)):
            diagonal = []
            i = row
            x = offset
            while i < len(input_grid[row]) and x < len(input_grid[row]):
                diagonal.append(input_grid[i][x])
                i += 1
                x += 1
            if len(diagonal) >= 3:
                diagonal_grid.append(diagonal)
    return diagonal_grid


# function to check for words found in rows against words in supplied_list and add to solution_list
def word_check(input_grid, supplied_woods, solution_list=[]):
    for row in input_grid:
        for word in supplied_woods:
            if word in "".join(row) or word in "".join(row[::-1]):
                bool = word in solution_list
                if bool == False:
                    solution_list.append(word)
    return solution_list


# function to print found words to console in required format
def print_found_words(answer):
    for word in answer:
        print(word)


def main():
    # create word list from input file
    word_list = create_word_list(input())

    # *grids*
    # create grid from input file
    grid = create_grid(input())
    # create column grid from original grid
    column_grid = create_column_grid(grid)
    # create diagonal grid from original grid
    diagonal_grid = create_diagonal_grid(grid)

    # *check for words*
    # horizontal
    horz_words = word_check(grid, word_list)
    # vertical
    vert_words = word_check(column_grid, word_list, horz_words)
    # diagonal
    all_words = word_check(diagonal_grid, word_list, vert_words)

    # print found words to console
    print_found_words(sorted(all_words))


main()
