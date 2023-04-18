mot = input("Entrez un mot sans espace ni caractère spécial : ")

# On transforme le mot en liste de caractères pour faciliter les modifications
liste_mot = list(mot)

# On compare chaque paire de caractères pour trouver le premier couple où le premier caractère est inférieur au deuxième
for i in range(len(liste_mot)-1):
    if liste_mot[i] < liste_mot[i+1]:
        # On recherche ensuite le caractère le plus petit dans la sous-liste à droite du caractère à échanger
        min_char = min(liste_mot[i+1:])
        # On échange les deux caractères
        index_min_char = liste_mot.index(min_char)
        liste_mot[i], liste_mot[index_min_char] = liste_mot[index_min_char], liste_mot[i]
        # On trie les caractères à droite de l'indice i en ordre croissant pour obtenir le mot le plus proche dans l'ordre alphabétique
        liste_mot[i+1:] = sorted(liste_mot[i+1:])
        # On affiche le nouveau mot obtenu
        print("Le mot le plus proche dans l'ordre alphabétique est :", ''.join(liste_mot))
        break
else:
    print("Aucun nouvel arrangement possible pour ce mot.")