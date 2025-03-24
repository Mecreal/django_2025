# Classe Flotte pour gérer un ensemble de véhicules

class Flotte:
    """Classe représentant une flotte de véhicules"""
    
    def __init__(self):
        """Constructeur de la classe Flotte"""
        self.vehicules = []  # Liste des véhicules dans la flotte
        self.convoi = False  # Mode convoi désactivé par défaut
    
    def ajouterVehicule(self, vehicule):
        """
        Ajoute un véhicule à la flotte
        
        Args:
            vehicule: Instance d'une classe dérivée de Vehicule
        """
        self.vehicules.append(vehicule)
        print(f"Véhicule {vehicule.immatriculation} ajouté à la flotte.")
    
    def afficher(self):
        """Affiche les informations de tous les véhicules de la flotte"""
        if not self.vehicules:
            print("La flotte est vide.")
            return
        
        print("\n=== FLOTTE DE VÉHICULES ===")
        print(f"Nombre de véhicules: {len(self.vehicules)}")
        print(f"Mode convoi: {'Activé' if self.convoi else 'Désactivé'}")
        if self.convoi:
            print(f"Vitesse du convoi: {self.vitesseFlotte()} km/h")
        print("\n--- Liste des véhicules ---")
        
        for i, vehicule in enumerate(self.vehicules, 1):
            print(f"\nVéhicule {i}:")
            vehicule.afficher()
            print("-" * 30)
    
    def vitesseFlotte(self):
        """
        Retourne la vitesse de la flotte en mode convoi
        
        Returns:
            int: Vitesse minimale des véhicules si en mode convoi, 0 sinon
        """
        if not self.convoi or not self.vehicules:
            return 0
        
        # La vitesse du convoi est la vitesse minimale de tous les véhicules
        vitesses = [vehicule.vitesseMaximale() for vehicule in self.vehicules]
        return min(vitesses)
    
    def positionneConvoi(self):
        """Active le mode convoi"""
        self.convoi = True
        print("Mode convoi activé. La flotte se déplace à la vitesse du véhicule le plus lent.")
    
    def enleveConvoi(self):
        """Désactive le mode convoi"""
        self.convoi = False
        print("Mode convoi désactivé. Les véhicules peuvent rouler à leur vitesse maximale.")
