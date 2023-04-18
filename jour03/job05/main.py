def nbres_premier(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 1001):
    if nbres_premier(i):
        print(i)