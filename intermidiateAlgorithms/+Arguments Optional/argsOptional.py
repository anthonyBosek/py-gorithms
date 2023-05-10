# Intermediate Algorithm Scripting: Arguments Optional
#
# Create a function that sums two arguments together. If only one argument is provided,
# then return a function that expects one argument and returns the sum. For example,
# addTogether(2, 3) should return 5, and addTogether(2) should return a function. Calling
# this returned function with a single argument will then return the sum:
# var sumTwoAnd = addTogether(2); sumTwoAnd(3) returns 5.
# If either argument isn't a valid number, return undefined.
#
# addTogether(val) ➞ num


def addTogether(x, y=None):
    if type(x) == int or type(x) == float:
        if y == None:
            return lambda y: x + y
        elif type(y) == int or type(y) == float:
            return x + y
        else:
            return None
    else:
        return None


print(addTogether(2, 3))  # ➞ 5
print(addTogether(2)(3))  # ➞ 5
print(addTogether("http://bit.ly/IqT6zt"))  # ➞ undefined
print(addTogether(2, "3"))  # ➞ undefined
print(addTogether(2)([3]))  # ➞ undefined

# Notes
#
# Closures
# Arguments object
