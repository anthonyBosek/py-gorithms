# Intermediate Algorithm Scripting: Sorted Union
#
# Write a function that takes two or more arrays and returns a new array of unique
# values in the order of the original provided arrays. In other words, all values
# present from all arrays should be included in their original order, but with no
# duplicates in the final array. The unique numbers should be sorted by their
# original order, but the final array should not be sorted in numerical order.
#
# uniteUnique(arr) ➞ arr


def uniteUnique(*arr):
    return list(set(sum(arr, [])))


print(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]))  # ➞ [1, 3, 2, 5, 4]
print(uniteUnique([1, 2, 3], [5, 2, 1]))  # ➞ [1, 2, 3, 5]
print(
    uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8])
)  # ➞ [1, 2, 3, 5, 4, 6, 7, 8]
