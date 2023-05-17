# List to string (Version 1)
#   Write a function concat_elements(slist, startpos, stoppos), where slist is a list of strings and
#   startpos and stoppos are integers, that concatenates the elements of slist starting at position
#   startpos and ending at position stoppos (inclusive) and returns the resulting string.
#
#   Your code should behave reasonably for all values of startpos and stoppos: if startpos is negative,
#    concatenation should start with the first element of slist; if stoppos ≥ len(slist), concatenation
#    should stop at the last element of slist. If startpos > stoppos it should return the empty string.
#    See the examples below.
#
#   Programming Requirements
#   -Solve this problem using a loop to iterate over the list.


# Solution
def concat_elements(slist, startpos, stoppos):
    result = ""
    if startpos > stoppos:
        return result
    if startpos < 0:
        startpos = 0
    if stoppos >= len(slist):
        stoppos = len(slist) - 1
    for i in range(len(slist)):
        if i >= startpos and i <= stoppos:
            result += slist[i]
    return result

    # Solution 1
    # result = ""
    # for i in range(startpos, stoppos + 1):
    #     if i >= len(slist):
    #         break
    #     result += slist[i]
    # return result

    # Solution 2
    # return "".join(slist[startpos : stoppos + 1])


# Examples
print(concat_elements(["aa", "bb", "cc", "dd"], 1, 3))  # ➞ 'bbccdd'
print(concat_elements(["aa", "bb", "cc", "dd"], -1, 1))  # ➞ 'aabb'
print(concat_elements(["aa", "bb", "cc", "dd"], -9, 9))  # ➞ 'aabbccdd'
print(concat_elements(["aa", "bb", "cc", "dd"], 3, 3))  # ➞ 'dd'
print(concat_elements(["aa", "bb", "cc", "dd"], 3, 1))  # ➞ ''
