num = [18, 3, 24, 63, 18, 4, 7]
newList = []
i = 0

while i < len(num):
    if num[i] % 2 == 1:
        newList.append(num[i])
        print(newList)
    i = i + 1

print(newList)
