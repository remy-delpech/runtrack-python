def distance_toilettes(marches, hauteur):
    distance_jour = (2 * marches * hauteur) / 100  # Distance parcourue pour aller et revenir une fois aux toilettes
    distance_semaine = distance_jour * 5 * 7  # Distance parcourue par semaine
    return round(distance_semaine, 2)

marches = 20
hauteur = 20
distance = distance_toilettes(marches, hauteur)
print(f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance} m par semaine.")