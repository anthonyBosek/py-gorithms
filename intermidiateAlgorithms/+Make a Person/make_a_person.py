# Intermediate Algorithm Scripting: Make a Person
#
# Fill in the object constructor with the following methods below:
#
#  getFirstName()
#  getLastName()
#  getFullName()
#  setFirstName(first)
#  setLastName(last)
#  setFullName(firstAndLast)
#
# Run the tests to see the expected output for each method. The methods that take an
# argument must accept only one argument and it has to be a string. These methods must
# be the only available means of interacting with the object.
#


class Person:
    def __init__(self, firstAndLast):
        self.firstName, self.lastName = firstAndLast.split(" ")

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFullName(self):
        return self.firstName + " " + self.lastName

    def setFirstName(self, first):
        self.firstName = first

    def setLastName(self, last):
        self.lastName = last

    def setFullName(self, newFirstAndLast):
        newFirst, newLast = newFirstAndLast.split(" ")
        self.firstName = newFirst
        self.lastName = newLast


bob = Person("Bob Ross")

print(len(bob.__dict__))  # ➞ 6
print(isinstance(bob, Person))  # ➞ True
print(bob.firstName)  # ➞ undefined
print(bob.lastName)  # ➞ undefined
print(bob.getFirstName())  # ➞ "Bob"
print(bob.getLastName())  # ➞ "Ross"
print(bob.getFullName())  # ➞ "Bob Ross"
bob.setFirstName("Haskell")
print(bob.getFullName())  # ➞ "Haskell Ross" after bob.setFirstName("Haskell")
bob.setLastName("Curry")
print(bob.getFullName())  # ➞ "Haskell Curry" after bob.setLastName("Curry")
bob.setFullName("Haskell Curry")
print(bob.getFullName())  # ➞ "Haskell Curry" after bob.setFullName("Haskell Curry")
print(bob.getFirstName())  # ➞ "Haskell" after bob.setFullName("Haskell Curry")
print(bob.getLastName())  # ➞ "Curry" after bob.setFullName("Haskell Curry")


# Other solutions
# class Person:
#     def __init__(self, firstAndLast):
#         self.firstAndLast = firstAndLast
#         self.firstName = firstAndLast.split(" ")[0]
#         self.lastName = firstAndLast.split(" ")[1]
#
#     def getFirstName(self):
#         return self.firstName
#
#     def getLastName(self):
#         return self.lastName
#
#     def getFullName(self):
#         return self.firstName + " " + self.lastName
#
#     def setFirstName(self, first):
#         self.firstName = first
#
#     def setLastName(self, last):
#         self.lastName = last
#
#     def setFullName(self, firstAndLast):
#         self.firstName = firstAndLast.split(" ")[0]
#         self.lastName = firstAndLast.split(" ")[1]
#
