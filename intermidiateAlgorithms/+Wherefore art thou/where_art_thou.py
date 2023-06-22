# Intermediate Algorithm Scripting: Wherefore art thou
#
# Make a function that looks through an array of objects (first argument) and returns an
# array of all objects that have matching name and value pairs (second argument). Each
# name and value pair of the source object has to be present in the object from the
# collection if it is to be included in the returned array.
#
# whatIsInAName(arr, obj) ➞ obj


# Solution 1
def whatIsInAName(collection, source):
    keys = list(source.keys())
    resultArr = []
    for obj in collection:
        all = True
        for key in keys:
            if key not in obj or obj[key] != source[key]:
                all = False
        if all == True:
            resultArr.append(obj)
    return resultArr


# # Solution 2
# def whatIsInAName(collection, source):
#     keys = list(source.keys())
#     return [
#         obj
#         for obj in collection
#         if all([key in obj and obj[key] == source[key] for key in keys])
#     ]


# # Solution 3
# def whatIsInAName(collection, source):
#     keys = list(source.keys())
#     return list(
#         filter(
#             lambda obj: all([key in obj and obj[key] == source[key] for key in keys]),
#             collection,
#         )
#     )


# # Solution 4
# def whatIsInAName(collection, source):
#     keys = list(source.keys())
#     return list(
#         filter(
#             lambda obj: all(
#                 map(lambda key: key in obj and obj[key] == source[key], keys)
#             ),
#             collection,
#         )
#     )


print(
    whatIsInAName(
        [
            {"first": "Romeo", "last": "Montague"},
            {"first": "Mercutio", "last": None},
            {"first": "Tybalt", "last": "Capulet"},
        ],
        {"last": "Capulet"},
    )
)
# ➞ [{ first: "Tybalt", last: "Capulet" }]

print(whatIsInAName([{"apple": 1}, {"apple": 1}, {"apple": 1, "bat": 2}], {"apple": 1}))
# ➞ [{ "apple": 1 }, { "apple": 1 }, { "apple": 1, "bat": 2 }]

print(
    whatIsInAName(
        [{"apple": 1, "bat": 2}, {"bat": 2}, {"apple": 1, "bat": 2, "cookie": 2}],
        {"apple": 1, "bat": 2},
    )
)
# ➞ [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie": 2 }]

print(
    whatIsInAName(
        [{"apple": 1, "bat": 2}, {"apple": 1}, {"apple": 1, "bat": 2, "cookie": 2}],
        {"apple": 1, "cookie": 2},
    )
)
# ➞ [{ "apple": 1, "bat": 2, "cookie": 2 }]

print(
    whatIsInAName(
        [
            {"apple": 1, "bat": 2},
            {"apple": 1},
            {"apple": 1, "bat": 2, "cookie": 2},
            {"bat": 2},
        ],
        {"apple": 1, "bat": 2},
    )
)
# ➞ [{ "apple": 1, "bat": 2 }, { "apple": 1, "bat": 2, "cookie":2 }]

print(whatIsInAName([{"a": 1, "b": 2, "c": 3}], {"a": 1, "b": 9999, "c": 3}))
# ➞ []
