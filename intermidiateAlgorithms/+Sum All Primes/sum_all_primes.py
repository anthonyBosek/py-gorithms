# Intermediate Algorithm Scripting: Sum All Primes
#
# Sum all the prime numbers up to and including the provided number. A prime number is
# defined as a number greater than one and having only two divisors, one and itself.
#
# sumPrimes(num) ➞ num


def sumPrimes(num):
    if num <= 1:
        return "Invalid Argument"
    sum = 2
    val = 3
    i = 2
    while val <= num:
        if val % i == 0:
            val += 1
            i = 1
        elif i >= int(val / 2):
            sum += val
            val += 1
            i = 1
        i += 1
    return sum


print(sumPrimes(1))  # ➞ Invalid Argument
print(sumPrimes(2))  # ➞ 2
print(sumPrimes(10))  # ➞ 17
print(sumPrimes(100))  # ➞ 1060
print(sumPrimes(977))  # ➞ 73156
