from vehicule import *

def main():
    # Créer deux camions avec des charges différentes
    c1 = Camion("CAM-001", 2022, 3)  # Camion avec charge de 3 tonnes
    c2 = Camion("CAM-002", 2023, 5)  # Camion avec charge de 5 tonnes
    
    # Créer un taxi
    t1 = Taxi("TAXI-001", 2024)
    
    # Afficher les véhicules
    print("=== INFORMATIONS DES VÉHICULES ===")
    print("\nCamion 1:")
    c1.setCharge(1)  # Modifier la charge du camion 1
    c1.afficher()

    print("\nCamion 2:")
    c2.afficher()
    
    print("\nTaxi:")
    t1.afficher()

if __name__ == "__main__":
    main()
