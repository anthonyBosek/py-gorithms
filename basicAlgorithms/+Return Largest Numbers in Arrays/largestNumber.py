# Basic Algorithm Scripting: Return Largest Numbers in Arrays
#
# Return an array consisting of the largest number from each provided sub-array.
# For simplicity, the provided array will contain exactly 4 sub-arrays.
#
# largestOfFour(arr) ➞ arr


def largestOfFour(arr):
    return list(map(lambda item: max(item), arr))


print(
    largestOfFour(
        [[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]
    )
)  # ➞ [ 5, 27, 39, 1001 ]
print(
    largestOfFour(
        [[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]
    )
)  # ➞ [27, 5, 39, 1001]
print(
    largestOfFour(
        [[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]
    )
)  # ➞ [9, 35, 97, 1000000]
print(
    largestOfFour(
        [[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]
    )
)  # ➞ [25, 48, 21, -3]
