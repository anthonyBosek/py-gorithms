# Intermediate Algorithm Scripting: Sum All Numbers in a Range
#
# We'll pass you an array of high numbers. Return the sum of those high numbers plus the
# sum of all the numbers between them. The lowest number will not always come first.
#
# sumAll(lst) ➞ num


def sumAll(lst):
    low = min(lst)
    high = max(lst)
    return sum(range(low, high + 1))


print(sumAll([1, 4]))  # ➞ 10
print(sumAll([4, 1]))  # ➞ 10
print(sumAll([5, 10]))  # ➞ 45
print(sumAll([10, 5]))  # ➞ 45
print(sumAll([7, 1]))  # ➞ 28
