# Column to list
#   Write a function column2list(grid, n), where grid is a list of lists and n is an integer,
#    that returns a list consisting of the element at position n of each row of grid.
#
#   You can assume that 0 ≤ n < len(r) for each row (i.e., element) of grid.
#


# Solution
def column2list(grid, n):
    result = []
    if n < 0:
        return result
    for i in range(len(grid)):
        if n >= len(grid[i]):
            break
        result.append(grid[i][n])
    return result


# Global Variables
x = [
    ["aa", "bb", "cc", "dd"],
    ["ee", "ff", "gg", "hh", "ii", "jj"],
    ["kk", "ll", "mm", "nn"],
    ["oo", "pp", "qq", "rr", "ss", "tt", "uu"],
    ["vv", "ww", "xx", "yy", "zz"],
]

# Examples
print(column2list(x, 1))  # ➞ [ 'bb', 'ff', 'll', 'pp', 'ww' ]
print(column2list(x, 3))  # ➞ ['dd', 'hh', 'nn', 'rr', 'yy' ]
print(column2list(x, 0))  # ➞ [ 'aa', 'ee', 'kk', 'oo', 'vv' ]
print(column2list(x, 9))  # ➞ []
print(column2list(x, -1))  # ➞ []
print(column2list(x, 2))  # ➞ ['cc', 'gg', 'mm', 'qq', 'xx']
