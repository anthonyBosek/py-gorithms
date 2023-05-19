# Grid is square


def grid_is_square(arglist):
    for i in range(len(arglist)):
        if len(arglist) != len(arglist[i]):
            return False
    return True


print(grid_is_square([[1, 2], [3, 4]]))
print(grid_is_square([[0, 1, 2], [3, 4]]))
print(grid_is_square([[0, 1, 2, 3, 4], [3, 4, 5, 6, 7], [4, 5, 6, 7, 8]]))
print(grid_is_square([[1]]))
print(grid_is_square([[1, 2, 3], [3, 4, 5], [5, 6, 7]]))
