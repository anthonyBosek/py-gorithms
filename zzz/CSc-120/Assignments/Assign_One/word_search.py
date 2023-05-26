# Word Serach

# word-list.txt file of words
# grid-of-letters.txt file of grid letters

# 1. Read in the word-list.txt file and store the words in a list.
# 2. Read in the grid-of-letters.txt file and store the letters in a list of lists.
# 3. For each word in the word list, search for it in the grid of letters.
# 4. If the word is found, append it to a list of found words.
# 5. Print the list of found words.


# def occurs_in(substr, word_list):
#     # ignore casing
#     # check horizontal
#     # check vertical
#     # check diagonal
#     return


def print_some_words(filename):
    textfile = open(filename)
    for line in textfile:
        line = line.split()
        print(line)


"""
# Word Serach

grid = []

def read_grid(filename):
    textfile = open(filename)
    for line in textfile:
        line = line.split()
        grid.append(line)
    print(grid)
    # return grid


def horizontal(filename):
    print("Printing words from " + filename)
    textfile = open(filename)
    for line in textfile:
        line = line.split()
        print(line)


def vertical(grid, n):
    result = []
    if n < 0:
        return result
    for i in range(len(grid)):
        if n >= len(grid[i]):
            break
        result.append(grid[i][n])
    return result


def main():
    read_grid("grid_02.txt")
    # for i in range(1, 10):
    #     print_some_words("grid_0" + str(i) + ".txt")


main()
  ________________________________________
#notes

# first open the two files
# then get the rows of letters from the grid
# create words of n lengths and chaeck against word list



def read_file(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()
    
def word_search():
    word_list = read_file("word-list.txt")
    grid = read_file("grid-of-letters.txt")
    print(word_list)
    print(grid)
    return

def test():
    word_search()
    return
"""


def main():
    # occurs_in()
    print_some_words("grid_03.txt")


main()
