def draw_tapis(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j or i+j == n:
                print('X', end='')
            else:
                print('.', end='')
        print()

draw_tapis(6)