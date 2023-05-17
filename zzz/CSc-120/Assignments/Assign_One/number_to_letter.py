# Number to letter
#   Write a function number2letter(n), where n is an integer between 0 and 25,
#   that returns the lower-case letter at position n. Here, 'a' is at position 0,
#   'b' is at position 1, 'c' is at position 2, ... 'z' is at position 25.
#
#   For example, number2letter(0) returns 'a', number2letter(1) returns 'b', and
#   number2letter(25) returns 'z'.
#
#   You can assume that the argument n is an integer between 0 and 25.
#
#   Hint: You can use the built-in function chr(n) to convert an integer n to the
#   corresponding character. For example, chr(97) returns 'a', chr(98) returns
#   'b', and chr(122) returns 'z'.


import string


# Solution
def number2letter(n):
    return string.ascii_lowercase[n]
    # return chr(n + 97)
    # return chr(ord("a") + n)


print(number2letter(0))  # ➞ 'a'
print(number2letter(1))  # ➞ 'b'
print(number2letter(3))  # ➞ 'd'
print(number2letter(17))  # ➞ 'r'
print(number2letter(25))  # ➞ 'z'
