# Intermediate Algorithm Scripting: Search and Replace
#
# Perform a search and replace on the sentence using the arguments provided and
# return the new sentence. First argument is the sentence to perform the search
# and replace on. Second argument is the word that you will be replacing (before).
# Third argument is what you will be replacing the second argument with (after).
# Notes:
#  • Preserve the case of the first character in the original word.
#
# myReplace(str, before, after) ➞ str


def myReplace(str, before, after):
    if before[0].isupper():
        after = after.capitalize()
    return str.replace(before, after)


print(myReplace("Let us go to the store", "store", "Mall"))  # ➞ "Let us go to the mall"
print(
    myReplace("He is Sleeping on the couch", "Sleeping", "sitting")
)  # ➞ "He is Sitting on the couch"
print(
    myReplace("This has a spellngi error", "spellngi", "spelling")
)  # ➞ "This has a spelling error"
print(myReplace("His name is Tom", "Tom", "john"))  # ➞ "His name is John"
print(
    myReplace("Let us get back to more Coding", "Coding", "algorithms")
)  # ➞ "Let us get back to more Algorithms"
