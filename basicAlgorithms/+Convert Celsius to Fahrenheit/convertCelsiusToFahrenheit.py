# Basic Algorithm Scripting: Convert Celsius to Fahrenheit
#
# The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius
# times 9/5, plus 32. You are given a variable celsius representing a temperature in
# Celsius. Use the variable fahrenheit already defined and assign it the Fahrenheit
# temperature equivalent to the given Celsius temperature. Use the algorithm mentioned
# above to help convert the Celsius temperature to Fahrenheit.
#
# convertToF(num) ➞ num


def convertToF(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


print(convertToF(0))  # return ➞ number
print(convertToF(-30))  # return ➞ -22
print(convertToF(-10))  # return ➞ 14
print(convertToF(0))  # return ➞ 32
print(convertToF(20))  # return ➞ 68
print(convertToF(30))  # return ➞ 86

# Notes
#
# Fahrenheit = Celsius * 9/5 + 32
# Only return the number
# Don't forget to return the result
# Run tests (ctrl + enter)
# Good luck!
#
