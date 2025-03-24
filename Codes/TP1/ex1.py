
# Demander à l'utilisateur de saisir le poids et la taille
poids = float(input("Votre poids en Kg:"))
taille = float(input("Votre taille en cm:"))

# Convertir la taille de cm en m
taille_m = taille / 100

# Calculer l'IMC
imc = poids / (taille_m ** 2)

# Afficher l'IMC
print(f"imc: {imc}")

# Afficher l'interprétation
if imc >= 40:
    print("Obésité morbide ou massive")
elif imc >= 35:
    print("Obésité sévère")
elif imc >= 30:
    print("Obésité modérée")
elif imc >= 25:
    print("Surpoids")
elif imc >= 18.5:
    print("Corpulence normale")
elif imc >= 16.5:
    print("Maigreur")
else:
    print("Famine")
