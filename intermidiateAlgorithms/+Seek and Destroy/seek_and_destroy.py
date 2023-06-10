# Intermediate Algorithm Scripting: Seek and Destroy
#
# You will be provided with an initial array (the first argument in the destroyer function),
# followed by one or more arguments. Remove all elements from the initial array that are of
# the same value as these arguments.
#
# destroyer(arr) ➞ arr


def destroyer(arr, *args):
    return [x for x in arr if x not in args]


print(destroyer([1, 2, 3, 1, 2, 3], 2, 3))  # ➞ [1, 1]
print(destroyer([1, 2, 3, 5, 1, 2, 3], 2, 3))  # ➞ [1, 5, 1]
print(destroyer([3, 5, 1, 2, 2], 2, 3, 5))  # ➞ [1]
print(destroyer([2, 3, 2, 3], 2, 3))  # ➞ []
print(destroyer(["tree", "hamburger", 53], "tree", 53))  # ➞ ["hamburger"]
print(
    destroyer(
        [
            "possum",
            "trollo",
            12,
            "safari",
            "hotdog",
            92,
            65,
            "grandma",
            "bugati",
            "trojan",
            "yacht",
        ],
        "yacht",
        "possum",
        "trollo",
        "safari",
        "hotdog",
        "grandma",
        "bugati",
        "trojan",
    )
)  # ➞ [12,92,65]
