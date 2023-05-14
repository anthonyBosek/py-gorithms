# Intermediate Algorithm Scripting: Convert HTML Entities
#
# Convert the characters &, <, >, " (double quote), and ' (apostrophe),
# in a string to their corresponding HTML entities.
#
# convertHTML(str) ➞ str


# ** for loop
def convertHTML(str):
    entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&apos;"}
    for char in str:
        if char in entities:
            str = str.replace(char, entities[char])
    return str


# ** list comprehension
# def convertHTML(str):
#     entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&apos;"}
#     return "".join([entities[char] if char in entities else char for char in str])

# ** map()
# def convertHTML(str):
#     entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&apos;"}
#     return "".join(map(lambda char: entities[char] if char in entities else char, str))

# ** map() with ternary operator
# def convertHTML(str):
#     entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&apos;"}
#     return "".join(map(lambda char: entities[char] if char in entities else char, str))

# ** map() with ternary operator and list comprehension
# def convertHTML(str):
#     entities = {"&": "&amp;", "<": "&lt;", ">": "&gt;", "\"": "&quot;", "'": "&apos;"}
#     return "".join([entities[char] if char in entities else char for char in str])

print(convertHTML("Dolce & Gabbana"))  # ➞ "Dolce &amp; Gabbana"
print(convertHTML("Hamburgers < Pizza < Tacos"))  # ➞ "Hamburgers &lt; Pizza &lt; Tacos"
print(convertHTML("Sixty > twelve"))  # ➞ "Sixty &gt; twelve"
print(
    convertHTML('Stuff in "quotation marks"')
)  # ➞ "Stuff in &quot;quotation marks&quot;"
print(convertHTML("Shindler's List"))  # ➞ "Shindler&apos;s List"
print(convertHTML("<>"))  # ➞ "&lt;&gt;"
print(convertHTML("abc"))  # ➞ "abc"

# Notes
# All test cases contain valid HTML entities.
# Don't use jQuery or other DOM methods.
# This is a good resource for escaping HTML entities in JS.
