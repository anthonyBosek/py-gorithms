# JavaScript Algorithms and Data Structures Projects: Palindrome Checker
#
# Return true if the given string is a palindrome. Otherwise, return false.
#
# palindrome(str) ➞ bool


def palindrome(str):
    forward = (
        str.lower()
        .replace(" ", "")
        .replace("_", "")
        .replace(",", "")
        .replace(".", "")
        .replace(":", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
        .replace("/", "")
        .replace("\\", "")
    )
    backward = forward[::-1]
    return True if forward == backward else False


print(palindrome("eye"))  # ➞ true
print(palindrome("_eye"))  # ➞ true
print(palindrome("race car"))  # ➞ true
print(palindrome("not a palindrome"))  # ➞ false
print(palindrome("A man, a plan, a canal. Panama"))  # ➞ true
print(palindrome("never odd or even"))  # ➞ true
print(palindrome("nope"))  # ➞ false
print(palindrome("almostomla"))  # ➞ false
print(palindrome("My age is 0, 0 si ega ym."))  # ➞ true
print(palindrome("1 eye for of 1 eye."))  # ➞ false
print(palindrome("0_0 (: /-\ :) 0-0"))  # ➞ true
print(palindrome("five|\_/|four"))  # ➞ false
