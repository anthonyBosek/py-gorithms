# Intermediate Algorithm Scripting: Sum All Odd Fibonacci Numbers
#
# Given a positive integer num, return the sum of all odd Fibonacci numbers
# that are less than or equal to num.
#
# sumFibs(num) ➞ num


def sumFibs(num):
    fibSeq = [1, 1]
    next = 0
    i = 0
    while next <= num:
        next = fibSeq[i] + fibSeq[i + 1]
        if next <= num:
            fibSeq.append(next)
        i += 1
    return sum([x for x in fibSeq if x % 2 != 0])


print(sumFibs(1))  # ➞ a number
print(sumFibs(4))  # ➞ 5
print(sumFibs(100))  # ➞ 188
print(sumFibs(1000))  # ➞ 1785
print(sumFibs(75024))  # ➞ 60696
print(sumFibs(75025))  # ➞ 135721
print(sumFibs(4000000))  # ➞ 4613732
