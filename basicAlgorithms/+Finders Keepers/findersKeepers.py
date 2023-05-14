# Basic Algorithm Scripting: Finders Keepers
#
# Create a function that looks through an array (first argument) and returns the first
# element in the array that passes a truth test (second argument). If no element passes
# the test, return undefined.
#
# findElement(arr, func) ➞ val


# ** for loop
def findElement(arr, func):
    for i in arr:
        if func(i):
            return i
    return None


# ** arr.filter()
# def findElement(arr, func):
#     return list(filter(func, arr))[0]

# ** arr.filter() with ternary operator
# def findElement(arr, func):
#     return list(filter(lambda x: x if func(x) else None, arr))[0]

# ** arr.filter() with ternary operator and list comprehension
# def findElement(arr, func):
#     return [x for x in arr if func(x)][0]


print(findElement([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0))  # ➞ 8
print(findElement([1, 3, 5, 9], lambda num: num % 2 == 0))  # ➞ None

# Notes
# Do not use the built-in .find() or .indexOf() methods.
# This challenge can be solved with the .filter() method.
