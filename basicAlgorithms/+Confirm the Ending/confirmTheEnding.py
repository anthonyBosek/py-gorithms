# Basic Algorithm Scripting: Confirm the Ending
#
# Check if a string (first argument, str) ends with the given target string
# (second argument, target). This challenge can be solved with the .endsWith() method,
# which was introduced in ES2015. But for the purpose of this challenge, we would like
# you to use one of the JavaScript substring methods instead.
#
# confirmEnding(str, str2) ➞ bool


def confirmEnding(str, str2):
    return True if str.endswith(str2) else False


print(confirmEnding("Bastian", "n"))  # ➞ true.
print(confirmEnding("Congratulation", "on"))  # ➞ true.
print(confirmEnding("Connor", "n"))  # ➞ false.
print(
    confirmEnding(
        "Walking on water and developing software from a specification are easy if both are frozen",
        "specification",
    )
)  # ➞ false.
print(confirmEnding("He has to give me a new name", "name"))  # ➞ true.
print(confirmEnding("Open sesame", "same"))  # ➞ true.
print(confirmEnding("Open sesame", "pen"))  # ➞ false.
print(confirmEnding("Open sesame", "game"))  # ➞ false.
print(
    confirmEnding(
        "If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing",
        "mountain",
    )
)  # ➞ false.
print(confirmEnding("Abstraction", "action"))  # ➞ true.

# Notes
#
# String.prototype.substr()
# String.prototype.substring()
