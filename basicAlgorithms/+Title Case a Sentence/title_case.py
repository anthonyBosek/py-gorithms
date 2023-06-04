# Basic Algorithm Scripting: Title Case a Sentence
#
# Return the provided string with the first letter of each word capitalized.
# Make sure the rest of the word is in lower case. For the purpose of this exercise,
# you should also capitalize connecting words like "the" and "of".
#
# titleCase(str) ➞ str


def titleCase(str):
    arr = str.lower().split(" ")
    for i in range(len(arr)):
        word = list(arr[i])
        word[0] = word[0].upper()
        arr[i] = "".join(word)
    return " ".join(arr)


print(titleCase("I'm a little tea pot"))  # ➞ "I'm A Little Tea Pot"
print(titleCase("sHoRt AnD sToUt"))  # ➞ "Short And Stout"
print(
    titleCase("HERE IS MY HANDLE HERE IS MY SPOUT")
)  # ➞ "Here Is My Handle Here Is My Spout"
