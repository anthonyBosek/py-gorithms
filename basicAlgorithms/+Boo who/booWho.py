# Basic Algorithm Scripting: Boo who
#
# Check if a value is classified as a boolean primitive. Return true or false.
# Boolean primitives are true and false.
#
# booWho(val) ➞ bool


def booWho(val):
    return True if type(val) == bool else False


print(booWho(True))  # ➞ true
print(booWho(False))  # ➞ true
print(booWho([1, 2, 3]))  # ➞ false
print(booWho({"a": 1}))  # ➞ false
print(booWho(1))  # ➞ false
print(booWho("a"))  # ➞ false
print(booWho("true"))  # ➞ false
print(booWho("false"))  # ➞ false

# Notes
#
# Boolean Objects
# Boolean Primitives
