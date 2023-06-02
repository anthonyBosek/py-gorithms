# Basic Algorithm Scripting: Reverse a String
#
# Reverse the provided string. You may need to turn the string into an array
# before you can reverse it. Your result must be a string.
#
# reverseString(str) ➞ str


def reverseString(str):
    return str[::-1]


print(reverseString("hello"))  # ➞ "olleh"
print(reverseString("Howdy"))  # ➞ "ydwoH"
print(reverseString("Greetings from Earth"))  # ➞ "htraE morf sgniteerG"
