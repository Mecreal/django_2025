def inverse_si_multiple_7(chaine:str)->str:
    if len(chaine) % 7 == 0:
        return chaine[::-1]
        # return reversed(chaine)
    else:
        return chaine
        

# # Test avec quelques exemples
# chaines_test = ["bonjour", "python", "informatique", "programmations"]

# for chaine in chaines_test:
#     resultat = inverse_si_multiple_7(chaine)
#     print(f"Chaîne d'origine: {chaine}, Longueur: {len(chaine)}")
#     print(f"Résultat: {resultat}")
#     print()

chaine = input("Entrez une chaîne de caractères: ")
resultat = inverse_si_multiple_7(chaine)
print(f"Chaîne d'origine: {chaine}, Longueur: {len(chaine)}")
print(f"Résultat: {resultat}")
print()
