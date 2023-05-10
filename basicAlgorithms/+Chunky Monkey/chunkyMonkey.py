# Basic Algorithm Scripting: Chunky Monkey
#
# Write a function that splits an array (first argument) into groups the length
# of size (second argument) and returns them as a two-dimensional array.
#
# chunkArrayInGroups(arr, size) ➞ arr


def chunkArrayInGroups(arr, size):
    resultArr = []
    for i in range(0, len(arr), size):
        resultArr.append(arr[i : i + size])
    return resultArr


print(chunkArrayInGroups(["a", "b", "c", "d"], 2))  # ➞ [["a", "b"], ["c", "d"]]
print(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3))  # ➞ [[0, 1, 2], [3, 4, 5]]

# Notes
#
# Arrays
# Array.prototype.slice()
