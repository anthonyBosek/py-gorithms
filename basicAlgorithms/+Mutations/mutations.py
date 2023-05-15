# Basic Algorithm Scripting: Mutations
#
# Return true if the string in the first element of the array contains all of
# the letters of the string in the second element of the array.
#
# mutation(arr) ➞ bool


def mutation(arr):
    fir, sec = arr
    return all(x in fir.lower() for x in sec.lower())


print(mutation(["hello", "hey"]))  # ➞ false
print(mutation(["hello", "Hello"]))  # ➞ true
print(mutation(["zyxwvutsrqponmlkjihgfedcba", "qrstu"]))  # ➞ true
print(mutation(["Mary", "Army"]))  # ➞ true
print(mutation(["Mary", "Aarmy"]))  # ➞ true
print(mutation(["Alien", "line"]))  # ➞ true
print(mutation(["floor", "for"]))  # ➞ true
print(mutation(["hello", "neo"]))  # ➞ false
print(mutation(["voodoo", "no"]))  # ➞ false
print(mutation(["ate", "date"]))  # ➞ false
print(mutation(["Tiger", "Zebra"]))  # ➞ false
print(mutation(["Noel", "Ole"]))  # ➞ true
