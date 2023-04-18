def arrondi_et_trie(liste):
    arrondis = []
    for nombre in liste:
        arrondi = int(nombre + 0.5)
        arrondis.append(arrondi)
    
    # Tri à bulles
    i = 0
    while i < len(arrondis):
        j = 0
        while j < len(arrondis) - i - 1:
            if arrondis[j] > arrondis[j+1]:
                arrondis[j], arrondis[j+1] = arrondis[j+1], arrondis[j]
                liste[j], liste[j+1] = liste[j+1], liste[j]
            j += 1
        i += 1
    
    return liste

liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
resultat = arrondi_et_trie(liste)
print(resultat)