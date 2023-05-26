def count_chars(s):
    counts = {}
    for elem in s:
        if elem in counts:
            counts[elem] = counts[elem] + 1
        else:
            counts[elem] = 1
        # print(counts)
    # print(counts)
    return counts


d = count_chars("aabbcc")
# print(d.keys())
# print(d.values())
x = list(d.items())
print(x)
print(type(x[0]))
