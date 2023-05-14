# Basic Algorithm Scripting: Find the Longest Word in a String
#
# Return the length of the longest word in the provided sentence.
# Your response should be a number.
#
# findLongestWordLength(str) ➞ num


def findLongestWordLength(str):
    arr = str.split(" ")
    arr.sort(key=len, reverse=True)
    return len(arr[0])


print(findLongestWordLength("The quick brown fox jumped over the lazy dog"))  # ➞ 6
print(findLongestWordLength("May the force be with you"))  # ➞ 5
print(findLongestWordLength("Google do a barrel roll"))  # ➞ 6
print(
    findLongestWordLength("What is the average airspeed velocity of an unladen swallow")
)  # ➞ 8
print(
    findLongestWordLength(
        "What if we try a super-long word such as otorhinolaryngology"
    )
)  # ➞ 19

# Notes
# This challenge can be solved with the .sort() method. If you'd like to challenge yourself, try to solve this challenge without using .sort().
# Remember to use Read-Search-Ask if you get stuck. Write your own code.
