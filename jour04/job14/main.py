def my_long_word(n, chaine):
    mots = chaine.split()
    resultat = ""
    for mot in mots:
        longueur_mot = 0
        for lettre in mot:
            longueur_mot += 1
        if longueur_mot > n:
            resultat += mot + " "
    return resultat.strip()

chaine = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
n = 3
resultat = my_long_word(n, chaine)
print(resultat)