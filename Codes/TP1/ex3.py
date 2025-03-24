def convertir_si_majuscules(chaine):
    count_maj = 0
    for i in range(min(4, len(chaine))):
        if chaine[i].isupper():
            count_maj += 1
    
    if count_maj >= 2:
        return chaine.upper()
    else:
        return chaine
        
        
# 2eme methode

# ~ def convertir_si_majuscules(chaine:str)->str:
    # ~ premiers = chaine[:4]
    # ~ count = 0
    # ~ for i in premiers:
        # ~ if 'A'<= i <='Z':
            # ~ count += 1

    # ~ if count >= 2:
        # ~ return chaine.upper()
    # ~ else:
        # ~ return chaine 

# Test avec quelques exemples
exemples = ["ABcd", "abCD", "abcd", "ABCdef", "AbCd", "Python"]

for exemple in exemples:
    resultat = convertir_si_majuscules(exemple)
    print(f"Chaîne d'origine: {exemple}")
    print(f"Résultat: {resultat}")
    print()
