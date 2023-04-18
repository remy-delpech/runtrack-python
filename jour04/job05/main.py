L = [2, 4, 6, 8, 10]
print(L[1])

def somme(L):
    L[3] = L[2] + L[4]
    print(L)
somme(L)

print(L[-1])