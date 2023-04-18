L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
calc = 1
for number in L:
    if number >= 25 and number <= 90:
        calc *= number
print(calc)