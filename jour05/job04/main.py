def chiffrement_cesar(message, decalage):
    message_chiffre = ''
    for lettre in message:
        if lettre.isalpha():
            # On calcule la nouvelle position de la lettre
            nouvelle_position = (ord(lettre) - ord('a') + decalage) % 26
            # On convertit la nouvelle position en lettre
            lettre_chiffree = chr(ord('a') + nouvelle_position)
        else:
            lettre_chiffree = lettre
        message_chiffre += lettre_chiffree
    return message_chiffre

message = "bonjour tout le monde"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(message_chiffre)