# Intermediate Algorithm Scripting: Pig Latin
#
# Translate the provided string to pig latin. Pig Latin takes the first consonant
# (or consonant cluster) of an English word, moves it to the end of the word and
# suffixes an "ay". If a word begins with a vowel you just add "way" to the end.
# If a word does not contain a vowel, just add "ay" to the end. Input strings are
# guaranteed to be English words in all lowercase.
#
# translatePigLatin(str) ➞ str


def translatePigLatin(str):
    if str[0] in "aeiou":
        return str + "way"
    else:
        for i in range(len(str)):
            if str[i] in "aeiou":
                return str[i:] + str[:i] + "ay"


print(translatePigLatin("california"))  # ➞ return "aliforniacay"
print(translatePigLatin("paragraphs"))  # ➞ return "aragraphspay"
print(translatePigLatin("glove"))  # ➞ return "oveglay"
print(translatePigLatin("algorithm"))  # ➞ return "algorithmway"
print(translatePigLatin("eight"))  # ➞ return "eightway"
print(translatePigLatin("schwartz"))  # ➞ return "artzschway"
print(translatePigLatin("rhythm"))  # ➞ return "rhythmay"
