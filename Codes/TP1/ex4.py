
# Définition des listes
vehicules = ["train", "bus", "voiture", "vélo"]
couleurs = ["rouge", "vert", "bleu", "jaune"]


lst = []
for vehicule in vehicules:
    for couleur in couleurs:
        if not (vehicule == "voiture" and couleur == "vert"):
            lst.append(f"{vehicule} {couleur}")


print("Liste de combinaisons (sans 'voiture vert'):")
for _ in lst:
    print(f"  - {_}")

print(f"\nNombre total de combinaisons: {len(lst)}")
