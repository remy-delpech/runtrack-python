L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max = L[0]
min = L[0]
for number in L:
    if number > max:
        max = number
    if number < min:
        min = number
print("maximum:", max)
print("minimum:", min)