L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
count = 0
for number in L:
    if number % 2 == 0:
        count += number
print(count)