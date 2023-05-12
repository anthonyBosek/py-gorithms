# JavaScript Algorithms and Data Structures Projects: Telephone Number Validator
#
# Return true if the passed string looks like a valid US phone number. The user may fill out the
# form field any way they choose as long as it has the format of a valid US number.The area code
# is required. If the country code is provided, you must confirm that the country code is 1.
#
# telephoneCheck(str) ➞ bool
import regex as re


def telephoneCheck(str):
    return (
        re.match(r"^1?[ -]?((\d{3})|\((\d{3})\))[ -]?(\d{3})[ -]?(\d{4})$", str)
        is not None
    )


print(telephoneCheck("555-555-5555"))  # ➞ a boolean
print(telephoneCheck("1 555-555-5555"))  # ➞ true
print(telephoneCheck("1 (555) 555-5555"))  # ➞ true
print(telephoneCheck("5555555555"))  # ➞ true
print(telephoneCheck("555-555-5555"))  # ➞ true
print(telephoneCheck("(555)555-5555"))  # ➞ true
print(telephoneCheck("1(555)555-5555"))  # ➞ true
print(telephoneCheck("555-5555"))  # ➞ false
print(telephoneCheck("5555555"))  # ➞ false
print(telephoneCheck("1 555)555-5555"))  # ➞ false
print(telephoneCheck("1 555 555 5555"))  # ➞ true
print(telephoneCheck("1 456 789 4444"))  # ➞ true
print(telephoneCheck("123**&!!asdf#"))  # ➞ false
print(telephoneCheck("55555555"))  # ➞ false
print(telephoneCheck("(6054756961)"))  # ➞ false
print(telephoneCheck("2 (757) 622-7382"))  # ➞ false
print(telephoneCheck("0 (757) 622-7382"))  # ➞ false
print(telephoneCheck("-1 (757) 622-7382"))  # ➞ false
print(telephoneCheck("2 757 622-7382"))  # ➞ false
print(telephoneCheck("10 (757) 622-7382"))  # ➞ false
print(telephoneCheck("27576227382"))  # ➞ false
print(telephoneCheck("(275)76227382"))  # ➞ false
print(telephoneCheck("2(757)6227382"))  # ➞ false
print(telephoneCheck("2(757)622-7382"))  # ➞ false
print(telephoneCheck("555)-555-5555"))  # ➞ false
print(telephoneCheck("(555-555-5555"))  # ➞ false
print(telephoneCheck("(555)5(55?)-5555"))  # ➞ false

# JavaScript Solution:
# const telephoneCheck = (str) => {
#     return /^1?[ -]?((\d{3})|\((\d{3})\))[ -]?(\d{3})[ -]?(\d{4})$/.test(str);
# }
#
# Explanation:
# ^1? - optional 1 at the beginning
# [ -]? - optional space or dash
# ((\d{3})|\((\d{3})\)) - 3 digits or (3 digits)
# [ -]? - optional space or dash
# (\d{3}) - 3 digits
# [ -]? - optional space or dash
# (\d{4}) - 4 digits
# $ - end of string
