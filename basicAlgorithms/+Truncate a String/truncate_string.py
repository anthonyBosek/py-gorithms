# Basic Algorithm Scripting: Truncate a String
#
# Truncate a string (first argument) if it is longer than the given maximum string
# length (second argument). Return the truncated string with a ... ending.
#
# truncateString(str, num) ➞ str


def truncateString(str, num):
    if num >= len(str):
        return str[:num]
    return str[:num] + "..."


print(
    truncateString("A-tisket a-tasket A green and yellow basket", 8)
)  # ➞ "A-tisket..."
print(
    truncateString("Peter Piper picked a peck of pickled peppers", 11)
)  # ➞ "Peter Piper..."
print(
    truncateString(
        "A-tisket a-tasket A green and yellow basket",
        len("A-tisket a-tasket A green and yellow basket"),
    )
)
# ➞ "A-tisket a-tasket A green and yellow basket"
print(
    truncateString(
        "A-tisket a-tasket A green and yellow basket",
        len("A-tisket a-tasket A green and yellow basket") + 2,
    )
)
# ➞ "A-tisket a-tasket A green and yellow basket"
print(truncateString("A-", 1))  # ➞ "A..."
print(truncateString("Absolutely Longer", 2))  # ➞ "Ab..."


# Solution by other challengers
#
# def truncateString(str, num):
#     return str[:num] + "..." if num < len(str) else str
#
# def truncateString(str, num):
#     if len(str) > num:
#         return str[:num] + "..."
#     return str
#
# def truncateString(str, num):
#     return str[:num] + "..." if len(str) > num else str
