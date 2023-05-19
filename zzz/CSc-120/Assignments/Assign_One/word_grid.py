# Word Grid

import random
import string

# from random import *


def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)
    make_grid(grid_size)
    # return grid_size


def make_grid(num):
    grid = []
    for i in range(num):
        row = []
        for j in range(num):
            x = random.randint(0, 25)
            row.append(string.ascii_lowercase[x])
        grid.append(row)
    print_grid(grid)
    # return grid


def print_grid(grid):
    for i in range(len(grid)):
        row = ",".join(grid[i])
        print(row)


def main():
    init()
    # print_grid(make_grid(init()))


main()
