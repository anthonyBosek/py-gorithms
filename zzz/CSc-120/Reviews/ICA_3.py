# Dictionary usage for reference:
# >>> d = {}
# >>> d['one'] = 1
# >>> d['two'] = 2
# >>> d['five'] = 5
# >>> 'three' in d
# False

d = {}
d["one"] = 1
d["two"] = 2
d["five"] = 5
print(d)

# ---------------------------------------------------------------

# 1. Write a loop to print the keys of d.


def print_keys(d):
    for key in d:
        print(key)


print_keys(d)


# ---------------------------------------------------------------

# 2. Write a loop to print the values in d two different ways:
# a) use the values() method
# b) don’t use the values() method


def print_values(d):
    # a) use the values() method
    for value in d.values():
        print(value)
    # b) don’t use the values() method
    for key in d:
        print(d[key])


print_values(d)

# ---------------------------------------------------------------

# 3. Write a function key_of_max_value(adict) that finds the maximum of all the values in
# the dictionary adict and returns the corresponding key. For example, if the dictionary passed
# in is
# {"hello" : 34, "sunny" : 51, "the" : 82, "street" : 13} returns 'the'.
# You’ll have to iterate through the dictionary and keep track of the maximum value seen so far,
# but also keep track of the corresponding key for that value.

sample_dict = {"hello": 134, "sunny": 51, "the": 82, "street": 13}
example_dict = {"hello": 34, "sunny": 51, "the": 82, "street": 13}
test_dict = {"hello": 34, "sunny": 51, "the": 82, "street": 113}


def key_of_max_value(adict):
    max_value = 0
    max_value_key = ""
    for key in adict:
        if adict[key] > max_value:
            max_value = adict[key]
            max_value_key = key
    return {max_value_key: max_value}
    # return max_value_key


print(key_of_max_value(sample_dict))
print(key_of_max_value(example_dict))
print(key_of_max_value(test_dict))

""" 
# sample solution from stackoverflow
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
# try to understand this solution
return {key: value for key, value in adict.items() if value == max(adict.values())}
"""

# ---------------------------------------------------------------

# 4. Create a function identify_unique_words(slist) that takes a list of strings slist.
# The function returns a dictionary where the keys are the strings in slist and the
# corresponding values are 0, if the string occurred only once in slist, and 1 otherwise. For
# example, if the function is called with the list
# ['here', 'is', 'the', 'root', 'of', 'the', 'root', 'and', 'the']
# then the dictionary returned is
# {'here': 0, 'is': 0, 'the': 1, 'root': 1, 'of': 0, 'and': 0}
# Notice that the strings that are unique in slist have a value of 0, and the words that are
# duplicates have a value of 1.

# ---------------------------------------------------------------
