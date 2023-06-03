# Basic Algorithm Scripting: Slice and Splice
#
# You are given two arrays and an index. Use the array methods slice and splice to
# copy each element of the first array into the second array, in order. Begin inserting
# elements at index n of the second array. Return the resulting array.
# The input arrays should remain the same after the function runs.
#
# frankenSplice(arr1, arr2, n) ➞ arr


def frankenSplice(arr1, arr2, n):
    arr2[n:n] = arr1
    return arr2


print(frankenSplice([1, 2, 3], [4, 5], 1))  # ➞ [4, 1, 2, 3, 5]
print(frankenSplice([1, 2], ["a", "b"], 1))  # ➞ ["a", 1, 2, "b"]
print(
    frankenSplice(["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2)
)  # ➞ ["head", "shoulders", "claw", "tentacle", "knees", "toes"]
