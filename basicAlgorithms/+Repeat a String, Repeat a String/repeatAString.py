# Basic Algorithm Scripting: Repeat a String Repeat a String
#
# Repeat a given string "str" (first argument) for "num" times (second argument).
# Return an empty string if num is not a positive number.
#
# repeatStringNumTimes(str,num) ➞ str


def repeatStringNumTimes(str, num):
    if num <= 0:
        return ""
    else:
        return str * num


print(repeatStringNumTimes("*", 3))  # ➞ "***"
print(repeatStringNumTimes("abc", 3))  # ➞ "abcabcabc"
print(repeatStringNumTimes("abc", 4))  # ➞ "abcabcabcabc"
print(repeatStringNumTimes("abc", 1))  # ➞ "abc"
print(repeatStringNumTimes("*", 8))  # ➞ "********"
print(repeatStringNumTimes("abc", -2))  # ➞ ""
print(repeatStringNumTimes("abc", 0))  # ➞ ""
