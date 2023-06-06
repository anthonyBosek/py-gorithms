# Intermediate Algorithm Scripting: Everything Be True
#
# Check if the predicate (second argument) is truthy on all elements of a collection (first argument).
# In other words, you are given an array collection of objects. The predicate pre will be an object
# property and you need to return true if its value is truthy. Otherwise, return false. In JavaScript,
# truthy values are values that translate to true when evaluated in a Boolean context. Remember, you
# can access object properties through either dot notation or [] notation.
#
# truthCheck(arr, str) ➞ bool


def truthCheck(collection, pre):
    for obj in collection:
        if not obj[pre]:
            return False
    return True


# Other solutions
# def truthCheck(collection, pre):
#     return all([obj[pre] for obj in collection])


# def truthCheck(collection, pre):
#     return all(map(lambda obj: obj[pre], collection))


# def truthCheck(collection, pre):
#     return all([obj.get(pre, False) for obj in collection])


# def truthCheck(collection, pre):
#     return all([pre in obj and obj[pre] for obj in collection])


# def truthCheck(collection, pre):
#     return all([pre in obj and bool(obj[pre]) for obj in collection])


# def truthCheck(collection, pre):
#     return all([pre in obj and obj[pre] is not None for obj in collection])


# def truthCheck(collection, pre):
#     return all(
#         [
#             pre in obj and obj[pre] is not None and obj[pre] is not False
#             for obj in collection
#         ]
#     )


# def truthCheck(collection, pre):
#     return all(
#         [
#             pre in obj
#             and obj[pre] is not None
#             and obj[pre] is not False
#             and obj[pre] is not ""
#             for obj in collection
#         ]
#     )


# def truthCheck(collection, pre):
#     return all(
#         [
#             pre in obj
#             and obj[pre] is not None
#             and obj[pre] is not False
#             and obj[pre] is not ""
#             and obj[pre] is not 0
#             for obj in collection
#         ]
#     )


# def truthCheck(collection, pre):
#     return all(
#         [
#             pre in obj
#             and obj[pre] is not None
#             and obj[pre] is not False
#             and obj[pre] is not ""
#             and obj[pre] is not 0
#             and obj[pre] is not []
#             for obj in collection
#         ]
#     )


print(
    truthCheck(
        [
            {"user": "Tinky-Winky", "sex": "male"},
            {"user": "Dipsy", "sex": "male"},
            {"user": "Laa-Laa", "sex": "female"},
            {"user": "Po", "sex": "female"},
        ],
        "sex",
    )
)  # ➞ true
print(
    truthCheck(
        [
            {"user": "Tinky-Winky", "sex": "male"},
            {"user": "Dipsy"},
            {"user": "Laa-Laa", "sex": "female"},
            {"user": "Po", "sex": "female"},
        ],
        "sex",
    )
)  # ➞ false
print(
    truthCheck(
        [
            {"user": "Tinky-Winky", "sex": "male", "age": 0},
            {"user": "Dipsy", "sex": "male", "age": 3},
            {"user": "Laa-Laa", "sex": "female", "age": 5},
            {"user": "Po", "sex": "female", "age": 4},
        ],
        "age",
    )
)  # ➞ false
print(
    truthCheck(
        [
            {"name": "Pete", "onBoat": true},
            {"name": "Repeat", "onBoat": true},
            {"name": "FastFoward", "onBoat": null},
        ],
        "onBoat",
    )
)  # ➞ false
print(
    truthCheck(
        [
            {"name": "Pete", "onBoat": true},
            {"name": "Repeat", "onBoat": true, "alias": "Repete"},
            {"name": "FastFoward", "onBoat": true},
        ],
        "onBoat",
    )
)  # ➞ true
print(truthCheck([{"single": "yes"}], "single"))  # ➞ true
print(truthCheck([{"single": ""}, {"single": "double"}], "single"))  # ➞ false
print(truthCheck([{"single": "double"}, {"single": undefined}], "single"))  # ➞ false
print(truthCheck([{"single": "double"}, {"single": NaN}], "single"))  # ➞ false
