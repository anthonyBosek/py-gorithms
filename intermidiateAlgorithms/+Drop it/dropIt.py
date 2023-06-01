# Intermediate Algorithm Scripting: Drop it
#
# Given the array arr, iterate through and remove each element starting from the
# first element (the 0 index) until the function func returns true when the iterated
# element is passed through it. Then return the rest of the array once the condition
# is satisfied, otherwise, arr should be returned as an empty array.
#
# dropElements(arr, func) ➞ arr


def dropElements(arr, func):
    for i in range(len(arr)):
        if func(arr[i]):
            break
        arr.pop(0)
    return arr


print(dropElements([1, 2, 3, 4], lambda n: n >= 3))  # ➞ [3, 4]
print(dropElements([0, 1, 0, 1], lambda n: n == 1))  # ➞ [1, 0, 1]
print(dropElements([1, 2, 3], lambda n: n > 0))  # ➞ [1, 2, 3]
print(dropElements([1, 2, 3, 4], lambda n: n > 5))  # ➞ []
print(dropElements([1, 2, 3, 7, 4], lambda n: n > 3))  # ➞ [7, 4]
print(dropElements([1, 2, 3, 9, 2], lambda n: n > 2))  # ➞ [3, 9, 2]

# Notes
# Do not use the built-in .filter() method.
# 1. Create a function that takes two arguments, an array and a function.
# 2. Iterate through the array.
# 3. If the function returns true for the current element, break out of the loop.
# 4. Otherwise, remove the current element from the array.
# 5. Return the modified array.
