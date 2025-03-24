# test_flotte.py - Application pour tester la classe Flotte

from vehicule import Camion, Fourgonnette, Bus, Taxi
from flotte import Flotte

def main():
    # Création d'une flotte
    ma_flotte = Flotte()
    
    # Création de véhicules variés
    c1 = Camion("CAM-001", 2022, 3)     # Camion avec 3 tonnes (vitesse: 90 km/h)
    c2 = Camion("CAM-002", 2023, 5)     # Camion avec 5 tonnes (vitesse: 80 km/h)
    f1 = Fourgonnette("FOUR-001", 2024) # Fourgonnette à vide (vitesse: 110 km/h)
    b1 = Bus("BUS-001", 2020, 30)       # Bus avec 30 passagers (vitesse: 100 km/h)
    t1 = Taxi("TAXI-001", 2021, 2)      # Taxi avec 2 passagers (vitesse: 130 km/h)
    
    # Ajout des véhicules à la flotte
    ma_flotte.ajouterVehicule(c1)
    ma_flotte.ajouterVehicule(c2)
    ma_flotte.ajouterVehicule(f1)
    ma_flotte.ajouterVehicule(b1)
    ma_flotte.ajouterVehicule(t1)
    
    # Affichage de la flotte (sans mode convoi)
    ma_flotte.afficher()
    
    # Activation du mode convoi
    print("\n--- Test du mode convoi ---")
    ma_flotte.positionneConvoi()
    print(f"Vitesse de la flotte en convoi: {ma_flotte.vitesseFlotte()} km/h")
    
    # Affichage de la flotte (avec mode convoi)
    ma_flotte.afficher()
    
    # Désactivation du mode convoi
    ma_flotte.enleveConvoi()
    
    # Modification des charges pour voir l'impact sur la vitesse du convoi
    print("\n--- Test avec modification des charges ---")
    c1.setCharge(0)  # Camion à vide (vitesse: 110 km/h)
    f1.setCharge(2)  # Fourgonnette avec charge (vitesse: 100 km/h)
    
    # Réactivation du mode convoi
    ma_flotte.positionneConvoi()
    print(f"Nouvelle vitesse de la flotte en convoi: {ma_flotte.vitesseFlotte()} km/h")

if __name__ == "__main__":
    main()
