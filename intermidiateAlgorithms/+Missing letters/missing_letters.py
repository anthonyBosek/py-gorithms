# Intermediate Algorithm Scripting: Missing letters
#
# Find the missing letter in the passed letter range and return it.
# If all letters are present in the range, return undefined.
#
# fearNotLetter(str) ➞ str

alphabet = ""

for i in range(97, 123):
    alphabet += chr(i)


def fearNotLetter(str):
    start = alphabet.index(str[0])
    end = start + len(str)
    cut = alphabet[start:end]
    return cut if str != cut else None


print(fearNotLetter("abce"))  # ➞ "d"
print(fearNotLetter("abcdefghjklmno"))  # ➞ "i"
print(fearNotLetter("stvwx"))  # ➞ "u"
print(fearNotLetter("bcdf"))  # ➞ "e"
print(fearNotLetter("abcdefghijklmnopqrstuvwxyz"))  # ➞ undefined


# const fearNotLetter = (str) => {
#     let start = alphabet.indexOf(str[0]);
#     let end = start + str.length;
#     let cut = alphabet.slice(start, end);
#     return str != cut ?
#         cut.split("").filter((x, i) => str.split("").indexOf(x) !== i)[0] :
#         undefined;
# }


# A-Z 65-90, a-z 97-122
# alphabetUpperCase = "";
# for i in range(65, 90):
#    alphabet += chr(i)
