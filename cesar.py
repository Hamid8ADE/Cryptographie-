def chiffrement_cesar(texte, decalage):
    resultat = ""
    for char in texte:
        if char.isalpha():
            majuscule = char.isupper()
            char = chr((ord(char) + decalage - ord('A' if majuscule else 'a')) % 26 + ord('A' if majuscule else 'a'))
        resultat += char
    return resultat

def dechiffrement_cesar(texte, decalage):
    return chiffrement_cesar(texte, -decalage)

# Demander à l'utilisateur d'entrer le texte original et le décalage
texte_original = input("Entrez le texte à chiffrer : ")
decalage = int(input("Entrez le décalage : "))

# Chiffrer et déchiffrer le texte
texte_chiffre = chiffrement_cesar(texte_original, decalage)
texte_dechiffre = dechiffrement_cesar(texte_chiffre, decalage)

# Afficher les résultats
print("Texte original:", texte_original)
print("Texte chiffré:", texte_chiffre)
print("Texte déchiffré:", texte_dechiffre)
