# Basic Algorithm Scripting: Falsy Bouncer
#
# Remove all falsy values from an array. Falsy values in JavaScript are false,
# null, 0, "", undefined, and NaN.
#
# bouncer(arr) ➞ newArr


def bouncer(arr):
    newArr = []
    for i in arr:
        if bool(i) == True:
            newArr.append(i)
    return newArr


print(bouncer([7, "ate", "", False, 9]))  # ➞ [7, "ate", 9]
print(bouncer(["a", "b", "c"]))  # ➞ ["a", "b", "c"]


# What is the python equivalent of NaN and undefined?
# print(bouncer([False, None, 0, NaN, undefined, ""]))  # ➞ []
# print(bouncer([1, None, NaN, 2, undefined]))  # ➞ [1, 2]
