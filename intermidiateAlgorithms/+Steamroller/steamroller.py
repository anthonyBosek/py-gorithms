# Intermediate Algorithm Scripting: Steamroller
#
# Flatten a nested array. You must account for varying levels of nesting.
#
# steamrollArray(arr) ➞ arr


def steamrollArray(arr):
    result = []
    for i in arr:
        if type(i) == list:
            result += steamrollArray(i)
        else:
            result.append(i)
    return result


print(steamrollArray([[["a"]], [["b"]]]))  # ➞ ["a", "b"]
print(steamrollArray([1, [2], [3, [[4]]]]))  # ➞ [1, 2, 3, 4]
print(steamrollArray([1, [], [3, [[4]]]]))  # ➞ [1, 3, 4]
print(steamrollArray([1, {}, [3, [[4]]]]))  # ➞ [1, {}, 3, 4]
