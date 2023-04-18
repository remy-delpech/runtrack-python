def tri_selection(liste):
    n = 0
    for _ in liste:
        n += 1
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

ma_liste = [5, 2, 8, 1, 3, 7]
print(tri_selection(ma_liste))