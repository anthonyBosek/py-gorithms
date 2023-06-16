# Intermediate Algorithm Scripting: Spinal Tap Case
#
# Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
#
# spinalCase(str) ➞ str

import re


def spinalCase(str):
    # return re.sub(r'(?<=[a-z])(?=[A-Z])|_| ', '-', str).lower()
    return re.sub(r"(?<=[a-z])(?=[A-Z])|_| ", "-", str).lower()


print(spinalCase("This Is Spinal Tap"))  # ➞ "this-is-spinal-tap"
print(spinalCase("thisIsSpinalTap"))  # ➞ "this-is-spinal-tap"
print(spinalCase("The_Andy_Griffith_Show"))  # ➞ "the-andy-griffith-show"
print(spinalCase("Teletubbies say Eh-oh"))  # ➞ "teletubbies-say-eh-oh"
print(spinalCase("AllThe-small Things"))  # ➞ "all-the-small-things"

print(spinalCase(" This Is Spinal Tap"))  # use .trim() to get ➞ "this-is-spinal-tap"
