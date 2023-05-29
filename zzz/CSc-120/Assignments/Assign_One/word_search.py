# Word Serach

# word-list.txt file of words
# grid-of-letters.txt file of grid letters

# 1. Read in the word-list.txt file and store the words in a list.
# 2. Read in the grid-of-letters.txt file and store the letters in a list of lists.
# 3. For each word in the word list, search for it in the grid of letters.
# 4. If the word is found, append it to a list of found words.
# 5. Print the list of found words.


# Word Search

word_list = []
grid = []
found_words = []


def create_word_list(filename):
    allWords = open(filename)
    for word in allWords:
        word_list.append(word.strip())
    allWords.close()


def print_found_words(answer):
    for word in answer:
        print(word)


def diagonal_check(g):
    # forward
    for row in g:
        for word in word_list:
            if word in "".join(row):
                if word in found_words:
                    continue
                else:
                    found_words.append(word)
    # backward
    for row in g:
        for word in word_list:
            if word in "".join(row[::-1]):
                found_words.append(word)
    print_found_words(sorted(found_words))


def vertical_check(g):
    # forward
    for row in g:
        for word in word_list:
            if word in "".join(row):
                found_words.append(word)
    # backward
    for row in g:
        for word in word_list:
            if word in "".join(row[::-1]):
                found_words.append(word)
    # print_found_words(sorted(found_words))


def horizontal_check(g):
    # forward
    for row in g:
        for word in word_list:
            if word in "".join(row):
                found_words.append(word)
    # backward
    for row in g:
        for word in word_list:
            if word in "".join(row[::-1]):
                found_words.append(word)


def create_diagonal_grid(g):
    diagonal_grid = []
    for row in range(len(g)):
        for offset in range(len(g)):
            diagonal = []
            i = row
            x = offset
            while i < len(g[row]) and x < len(g[row]):
                diagonal.append(g[i][x])
                i += 1
                x += 1
            if len(diagonal) >= 3:
                diagonal_grid.append(diagonal)
    return diagonal_grid


def create_column_grid(g):
    column_grid = []
    for i in range(len(g)):
        column = []
        for j in range(len(g[i])):
            column.append(g[j][i])
        column_grid.append(column)
    return column_grid


def create_grid(filename):
    sampleGrid = open(filename)
    for line in sampleGrid:
        line = line.split()
        grid.append(line)
    sampleGrid.close()
    horizontal_check(grid)
    vertical_check(create_column_grid(grid))
    diagonal_check(create_diagonal_grid(grid))


def main():
    for i in range(1, 11):
        create_word_list("dict.txt")
        if i > 9:
            testCase = "grid_" + str(i) + ".txt"
        else:
            testCase = "grid_0" + str(i) + ".txt"
        print(testCase)
        create_grid(testCase)
        word_list.clear()
        grid.clear()
        found_words.clear()


main()
