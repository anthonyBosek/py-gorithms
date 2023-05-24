# 1. Write a for loop that
#   a. prints the numbers from 100 to 0 in descending order by 2
#   b. prints every other element of nums , which is a list of integers

# # Solution a.
# for i in range(100, -1, -2):
# for i in range(100, -2, -2):
#     print(i)

# # Solution b.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0,len(nums),2):
# for i in nums[::2]:
#     print(i)


# ---------------------------------------------------------------

# 2. Write a function get_words(s) that takes a string s as an argument that
#   consists of words separated by dashes. The function get_words returns a list of
#   strings where each string in the list is one of the words in s. For example,
#       get_words('CS-120-Summer-2018-U-of-A')
#   returns
#       ['CS', '120', 'Summer', 2018', 'U', 'of', 'A']


# Solution
# def get_words(s):
#     return s.split("-")


# print(
#     get_words("CS-120-Summer-2018-U-of-A")
# )  # ➞ ['CS', '120', 'Summer', '2018', 'U', 'of', 'A']


# ---------------------------------------------------------------

# 3. Write a function sum_column(grid, offset) that takes as
#   arguments a grid of numbers and an offset and returns the result of
#   summing the numbers on a specified column of grid. A grid is
#   represented as a list of lists, as shown on the right, and offset 0 refers
#   to the leftmost column (in the example shown: 11, 66, 22, 77, 33).
#   You can assume that the argument grid is in fact a grid (i.e., a list of
#   equal-length lists of numbers)

# myGrid = [
#     [11, 22, 33, 44, 55],
#     [66, 77, 88, 99, 11],
#     [22, 33, 44, 55, 66],
#     [77, 88, 99, 11, 22],
#     [33, 44, 55, 66, 77],
# ]


# Solution
# def sum_column(grid, offset):
#     sum = 0
#     for i in range(len(grid)):
#         sum += grid[i][offset]
#     return sum

# Alternate Solution
# def sum_column(grid, offset):
# return sum([row[offset] for row in grid])


# print(sum_column(myGrid, 0))  # ➞ 209


# ---------------------------------------------------------------

# 4. Write a function print_some_words(filename,n) that takes a filename
#     as a string argument and for each line in the file, finds and prints the individual
#     words of length great than or equal to n on a separate line.
#     A word is defined as a string of characters separated by white space. When
#     considering words, the punctuation characters ".,;?" should be omitted. For
#     example, if the file poem.txt consists of the following lines,
#
#           Two roads diverged in a yellow wood,
#           And sorry I could not travel both
#           And be one traveler, long I stood
#           And looked down one as far as I could
#           To where it bent in the undergrowth;
#
# the function print_some_words(“poem.txt”, 6)would print the words below:
#
#           diverged
#           yellow
#           travel
#           traveler
#           looked
#           undergrowth


# Solution
def print_some_words(filename, n):
    textfile = open(filename)
    for line in textfile:
        line = line.split()
        for word in line:
            clean_word = word.strip(".,?;")
            if len(clean_word) >= n:
                print(clean_word)


# Alternate Solution
# def print_some_words(filename, n):
#     with open(filename, "r") as f:
#         for line in f:
#             for word in line.split():
#                 if len(word) >= n:
#                     print(word)


print_some_words("sample.txt", 6)


# ---------------------------------------------------------------
# 5. Challenge. Write a function sum_diag_UL_LR(grid, offset) that takes as
#   arguments a grid of numbers and an offset and returns the result of summing the numbers on a specified
#   diagonal of grid. This function considers diagonals running from the upper-left of the grid to the lowerright
#   (hence the ‘UL_LR’ in the function name). The offset is used to select which diagonal to sum, as shown on
#   the right; the grid shown in this figure is represented in the program as a list of lists:
#           [ [11, 22, 33, 44, 55],
#             [66, 77, 88, 99, 11],
#             [22, 33, 44, 55, 66],
#             [77, 88, 99, 11, 22],
#             [33, 44, 55, 66, 77] ]
#
# Your program can assume that the argument grid is in fact a grid (i.e., a list of
#   equal-length lists of numbers) but should be able to handle grids of any size.
#
# Hint: Start by writing out the indices of the diagonals for each offset. First do the
#   positive offsets and write the code for the positive offsets.


# myGrid = [
#     [11, 22, 33, 44, 55],
#     [66, 77, 88, 99, 11],
#     [22, 33, 44, 55, 66],
#     [77, 88, 99, 11, 22],
#     [33, 44, 55, 66, 77],
# ]


# # Solution
# def sum_diag_UL_LR(grid, offset):
#     sum = 0
#     if offset > 0:
#         i = 0
#         x = offset
#         while i < len(grid) and x < len(grid[i]):
#             sum += grid[i][x]
#             i += 1
#             x += 1
#     else:
#         i = -offset
#         x = 0
#         while i < len(grid) and x < len(grid[i]):
#             sum += grid[i][x]
#             i += 1
#             x += 1
#     return sum


# print(sum_diag_UL_LR(myGrid, 2))  # ➞ 198
# print(sum_diag_UL_LR(myGrid, -2))  # ➞ 165
# print(sum_diag_UL_LR(myGrid, 0))  # ➞ 220
# print(sum_diag_UL_LR(myGrid, -3))  # ➞ 121


#
# ---------------------------------------------------------------

# Notes
"""
offset = 0
grid[0][0]
grid[1][1]
grid[2][2]
grid[3][3]
grid[4][4]

offset = 1
grid[0][1]
grid[1][2]
grid[2][3]
grid[3][4]

offset = 2
grid[0][2]
grid[1][3]
grid[2][4]
"""
"""
for i in range(len(grid)):
    print(grid[i][i])

from coursework------------------------------------------------
 sum = 0
 if offset > 0:
 # write the code for the positive case
 else:
 # write the code for the negative case

 def sum_diag_UL_LR(grid, offset):
 sum = 0
 if offset > 0:
 i,j = 0,offset
 else:
 i,j = -offset,0
 while i < len(grid) and j < len(grid): # both indexes within
bounds
 sum += grid[i][j]
 i, j = i+1, j+1
 return sum
--------------------------------------------------------------

notes**5/15
while loop
i & j
positive offsets
negative offsets
and combine
"""

# Alternate Solution
# def sum_diag_UL_LR(grid, offset):
#     sum = 0
#     for i in range(len(grid)):
#         sum += grid[i][i + offset]
#     return sum
