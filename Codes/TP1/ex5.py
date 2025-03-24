def nettoyage(liste1, val):
    """
    Retourne une nouvelle liste sans les occurrences de val
    
    Args:
        liste1: liste d'origine
        val: valeur à supprimer
        
    Returns:
        Une nouvelle liste sans les occurrences de val
    """
    return [element for element in liste1 if element != val]


def carreListe(lst):
    """
    Remplace directement dans la liste toutes les valeurs négatives par leur carré
    
    Args:
        lst: liste à modifier
    """
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] **= 2

# Tests des fonctions
print("Test de la fonction nettoyage:")
liste_test1 = [1, 2, 3, 2, 4, 2, 5]
val_test = 2
resultat = nettoyage(liste_test1, val_test)
print(f"Liste originale: {liste_test1}")
print(f"Après nettoyage de {val_test}: {resultat}")
print()

print("Test de la fonction carreListe:")
liste_test2 = [1, -2, 3, -4, 5, -6]
print(f"Liste avant: {liste_test2}")
carreListe(liste_test2)
print(f"Liste après: {liste_test2}")
