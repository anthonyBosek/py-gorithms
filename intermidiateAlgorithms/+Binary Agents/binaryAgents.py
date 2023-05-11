# Intermediate Algorithm Scripting: Binary Agents
#
# Return an English translated sentence of the passed binary string.
# The binary string will be space separated.
#
# binaryAgent(str) ➞ str


def binaryAgent(str):
    return "".join([chr(int(x, 2)) for x in str.split(" ")])


print(
    binaryAgent(
        "01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"
    )
)  #  "Aren't bonfires fun!?"

print(
    binaryAgent(
        "01001001 00100000 01101100 01101111 01110110 01100101 00100000 01010000 01100101 01110010 01110011 01100101 01110110 01100101 01110010 01100101 00100000 01000011 01101111 01100100 01100101 00100000 01000011 01100001 01101101 01110000 00100001"
    )
)  #  "I love Persevere Code Camp!"

# Notes
#
# String.prototype.charCodeAt()
# String.fromCharCode()
