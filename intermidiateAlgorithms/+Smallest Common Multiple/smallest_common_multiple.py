# Intermediate Algorithm Scripting: Smallest Common Multiple
#
# Find the smallest common multiple of the provided parameters that can be evenly
# divided by both, as well as by all sequential numbers in the range between these
# parameters. The range will be an array of two numbers that will not necessarily
# be in numerical order.
#
# smallestCommons(arr) ➞ num


def smallestCommons(arr):
    start, stop = sorted(arr)
    num = stop
    for i in range(start, stop + 1):
        if num % i != 0:
            num += stop
            i = start - 1
    return num


print(smallestCommons([1, 5]))  # ➞ 60
print(smallestCommons([5, 1]))  # ➞ 60
print(smallestCommons([2, 10]))  # ➞ 2520
print(smallestCommons([1, 13]))  # ➞ 360360
print(smallestCommons([23, 18]))  # ➞ 6056820
