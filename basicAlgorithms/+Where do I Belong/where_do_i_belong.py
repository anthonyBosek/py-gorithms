# Basic Algorithm Scripting: Where do I Belong
#
# Return the lowest index at which a value (second argument) should be inserted
# into an array (first argument) once it has been sorted. The returned value should
# be a number.
#
# getIndexToIns(arr, num) ➞ num


def getIndexToIns(arr, num):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] >= num:
            return i
    return len(arr)


print(getIndexToIns([10, 20, 30, 40, 50], 35))  # ➞ 3
print(getIndexToIns([10, 20, 30, 40, 50], 30))  # ➞ 2
print(getIndexToIns([40, 60], 50))  # ➞ 1
print(getIndexToIns([3, 10, 5], 3))  # ➞ 0
print(getIndexToIns([5, 3, 20, 3], 5))  # ➞ 2
print(getIndexToIns([2, 20, 10], 19))  # ➞ 2
print(getIndexToIns([2, 5, 10], 15))  # ➞ 3
print(getIndexToIns([], 1))  # ➞ 0

# Solution by other challengers
#
# def getIndexToIns(arr, num):
#     arr.append(num)
#     arr.sort()
#     return arr.index(num)
