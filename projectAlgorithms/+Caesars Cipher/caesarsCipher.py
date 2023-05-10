# JavaScript Algorithms and Data Structures Projects: Caesars Cipher
#
# One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift
# cipher. In a shift cipher the meanings of the letters are shifted by some set amount. A common
# modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places.
# Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on. Write a function which takes a ROT13 encoded string as
# input and returns a decoded string. All letters will be uppercase. Do not transform any
# non-alphabetic character (i.e. spaces, punctuation), but do pass them on.
#
# rot13(str) ➞ str


def rot13(str):
    alphabet = ""
    for i in range(65, 91):
        alphabet += chr(i)
    ciphabet = alphabet[13 : len(alphabet)] + alphabet[0:13]
    return "".join([x if not x.isalpha() else ciphabet[alphabet.index(x)] for x in str])


print(rot13("LBH QVQ VG!"))  # ➞ "YOU DID IT!"
print(rot13("SERR PBQR PNZC"))  # ➞ "FREE CODE CAMP"
print(rot13("SERR CVMMN!"))  # ➞ "FREE PIZZA!"
print(rot13("SERR YBIR?"))  # ➞ "FREE LOVE?"
print(
    rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.")
)  # ➞ "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."

# Notes
#
# A = 65
# Z = 90
# a = 97
# z = 122
