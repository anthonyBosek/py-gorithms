# Intermediate Algorithm Scripting: Diff Two Arrays
#
# Compare two arrays and return a new array with any items only found in one of
# the two given arrays, but not both. In other words, return the symmetric
# difference of the two arrays.
#
# diffArray(arr1, arr2) ➞ arr


# ** arr1.map() and arr2.indexOf()
def diffArray(arr1, arr2):
    justOne = []
    for x in arr1:
        if arr2.index(x) < 0:
            justOne.append(x)
    for x in arr2:
        if arr1.index(x) < 0:
            justOne.append(x)
    return justOne


# ** arr1.map() and arr2.indexOf() with ternary operator
# def diffArray(arr1, arr2):
#     justOne = []
#     for x in arr1:
#         justOne.append(x) if arr2.index(x) < 0 else None
#     for x in arr2:
#         justOne.append(x) if arr1.index(x) < 0 else None
#     return justOne


# ** arr1.map() and arr2.indexOf() with ternary operator and list comprehension
# def diffArray(arr1, arr2):
#     justOne = []
#     [justOne.append(x) if arr2.index(x) < 0 else None for x in arr1]
#     [justOne.append(x) if arr1.index(x) < 0 else None for x in arr2]
#     return justOne


print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))  # ➞  an array
print(
    diffArray(
        ["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
        ["diorite", "andesite", "grass", "dirt", "dead shrub"],
    )
)  # ➞  ["pink wool"]
print(
    diffArray(
        ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
        ["diorite", "andesite", "grass", "dirt", "dead shrub"],
    )
)  # ➞  ["diorite", "pink wool"]
print(
    diffArray(
        ["andesite", "grass", "dirt", "dead shrub"],
        ["andesite", "grass", "dirt", "dead shrub"],
    )
)  # ➞  []
print(diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5]))  # ➞  [4]
print(diffArray([1, "calf", 3, "piglet"], [1, "calf", 3, 4]))  # ➞  ["piglet", 4]
print(
    diffArray([], ["snuffleupagus", "cookie monster", "elmo"])
)  # ➞  ["snuffleupagus", "cookie monster", "elmo"]
print(
    diffArray([1, "calf", 3, "piglet"], [7, "filly"])
)  # ➞  [1, "calf", 3, "piglet", 7, "filly"]
