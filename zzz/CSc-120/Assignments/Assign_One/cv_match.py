# cv_match


def cv_match(sentence, pattern):
    vowels = "aeiou"
    words = sentence.split(" ")
    result = []
    for i in range(len(words)):
        if len(words[i]) == len(pattern):
            for j in range(len(words[i])):
                if pattern[j] == "v" and words[i][j] not in vowels:
                    break
                if j == len(words[i]) - 1:
                    result.append(words[i])
    return result


print(
    cv_match("Tim has a pet rat named Nip", "cvc")
)  # ➞ ['Tim', 'has', 'pet', 'rat', 'Nip']
print(cv_match("Put the loot in your boot", "cvvc"))  # ➞ ['loot', 'your', 'boot']
print(cv_match("This will have no matches", "vvv"))  # ➞ []
print(cv_match("This will have matches latches", "cvcccvc"))  # ➞ [matches, latches]
print(cv_match("This will have gave matches", "cvcv"))  # ➞ [have, gave]
