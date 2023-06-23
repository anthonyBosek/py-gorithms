# JavaScript Algorithms and Data Structures Projects: Roman Numeral Converter
#
# Convert the given number into a roman numeral.
# All roman numerals answers should be provided in upper-case.
#
# convertToRoman(num) ➞ str


def convertToRoman(num):
    conversion = [
        {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        },
        {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC",
        },
        {
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
        },
        {
            0: "",
            1: "M",
            2: "MM",
            3: "MMM",
            4: "M⊽",
            5: "⊽",
            6: "⊽M",
            7: "⊽MM",
            8: "⊽MMM",
            9: "??",
        },
    ]
    # solution with map()
    return "".join(
        list(map(lambda x: conversion[x[0]][int(x[1])], enumerate(reversed(str(num)))))
    )

    # solution with for loop
    # arr = list(reversed(str(num)))
    # roman = ""
    # for i in range(len(arr)-1, -1, -1):
    #     roman += conversion[i][int(arr[i])]
    # return roman


print(convertToRoman(2))  # ➞ "II"
print(convertToRoman(3))  # ➞ "III"
print(convertToRoman(4))  # ➞ "IV"
print(convertToRoman(5))  # ➞ "V"
print(convertToRoman(9))  # ➞ "IX"
print(convertToRoman(12))  # ➞ "XII"
print(convertToRoman(16))  # ➞ "XVI"
print(convertToRoman(29))  # ➞ "XXIX"
print(convertToRoman(44))  # ➞ "XLIV"
print(convertToRoman(45))  # ➞ "XLV"
print(convertToRoman(68))  # ➞ "LXVIII"
print(convertToRoman(83))  # ➞ "LXXXIII"
print(convertToRoman(97))  # ➞ "XCVII"
print(convertToRoman(99))  # ➞ "XCIX"
print(convertToRoman(400))  # ➞ "CD"
print(convertToRoman(500))  # ➞ "D"
print(convertToRoman(501))  # ➞ "DI"
print(convertToRoman(649))  # ➞ "DCXLIX"
print(convertToRoman(798))  # ➞ "DCCXCVIII"
print(convertToRoman(891))  # ➞ "DCCCXCI"
print(convertToRoman(1000))  # ➞ "M"
print(convertToRoman(1004))  # ➞ "MIV"
print(convertToRoman(1006))  # ➞ "MVI"
print(convertToRoman(1023))  # ➞ "MXXIII"
print(convertToRoman(2014))  # ➞ "MMXIV"
print(convertToRoman(3999))  # ➞ "MMMCMXCIX"
