# Classes pour les véhicules

class Vehicule:
    """Classe de base pour tous les véhicules"""
    
    def __init__(self, immatriculation:str, annee_achat:int, poids_vide:int):
        """
        Constructeur de la classe Vehicule
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            poids_vide (int): Poids à vide en tonnes
        """
        self.immatriculation = immatriculation
        self.annee_achat = annee_achat
        self.poids_vide = poids_vide
    
    def afficher(self) -> None:
        """Affiche les informations du véhicule"""
        print(f"Immatriculation: {self.immatriculation}")
        print(f"Année d'achat: {self.annee_achat}")
        print(f"Poids à vide: {self.poids_vide} tonnes")
        print(f"Vitesse maximale: {self.vitesseMaximale()} km/h")
    
    def vitesseMaximale(self) -> int:
        """Retourne la vitesse maximale du véhicule"""
        return 0  # À surcharger dans les classes dérivées


class VehiculeTransportMarchandise(Vehicule):
    """Classe pour les véhicules de transport de marchandises"""
    
    def __init__(self, immatriculation, annee_achat, poids_vide, charge_max):
        """
        Constructeur de la classe VehiculeTransportMarchandise
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            poids_vide (int): Poids à vide en tonnes
            charge_max (float): Charge maximale en tonnes
        """
        super().__init__(immatriculation, annee_achat, poids_vide)
        self.charge_max = charge_max
        self.charge_actuelle = 0
    
    def afficher(self):
        """Affiche les informations du véhicule de transport de marchandises"""
        super().afficher()
        print(f"Charge maximale: {self.charge_max} tonnes")
        print(f"Charge actuelle: {self.charge_actuelle} tonnes")
    
    def setCharge(self, charge):
        """
        Définit la charge actuelle du véhicule
        
        Args:
            charge (float): Charge en tonnes
        """
        if 0 <= charge <= self.charge_max:
            self.charge_actuelle = charge
        else:
            print(f"Erreur: La charge doit être entre 0 et {self.charge_max} tonnes")


class Fourgonnette(VehiculeTransportMarchandise):
    """Classe pour les fourgonnettes"""
    
    def __init__(self, immatriculation, annee_achat):
        """
        Constructeur de la classe Fourgonnette
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
        """
        super().__init__(immatriculation, annee_achat, 2, 3)  # 2 tonnes à vide, 3 tonnes max
    
    def vitesseMaximale(self):
        """Retourne la vitesse maximale de la fourgonnette selon sa charge"""
        if self.charge_actuelle > 0:
            return 100  # 100 km/h avec charge
        else:
            return 110  # 110 km/h à vide


class Camion(VehiculeTransportMarchandise):
    """Classe pour les camions"""
    
    def __init__(self, immatriculation, annee_achat, charge=0):
        """
        Constructeur de la classe Camion
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            charge (float, optional): Charge actuelle en tonnes. Defaults to 0.
        """
        super().__init__(immatriculation, annee_achat, 5, 6)  # 5 tonnes à vide, 6 tonnes max
        self.setCharge(charge)
    
    def vitesseMaximale(self):
        """Retourne la vitesse maximale du camion selon sa charge"""
        if self.charge_actuelle == 0:
            return 110  # 110 km/h à vide
        elif self.charge_actuelle <= 3:
            return 90   # 90 km/h avec charge ≤ 3 tonnes
        else:
            return 80   # 80 km/h avec charge > 3 tonnes


class VehiculeTransportPassagers(Vehicule):
    """Classe pour les véhicules de transport de passagers"""
    
    def __init__(self, immatriculation, annee_achat, poids_vide, capacite_max):
        """
        Constructeur de la classe VehiculeTransportPassagers
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            poids_vide (int): Poids à vide en tonnes
            capacite_max (int): Capacité maximale en nombre de passagers
        """
        super().__init__(immatriculation, annee_achat, poids_vide)
        self.capacite_max = capacite_max
        self.nb_passagers = 0
    
    def afficher(self):
        """Affiche les informations du véhicule de transport de passagers"""
        super().afficher()
        print(f"Capacité maximale: {self.capacite_max} passagers")
        print(f"Nombre actuel de passagers: {self.nb_passagers}")
    
    def setPassagers(self, nb_passagers):
        """
        Définit le nombre de passagers
        
        Args:
            nb_passagers (int): Nombre de passagers
        """
        if 0 <= nb_passagers <= self.capacite_max:
            self.nb_passagers = nb_passagers
        else:
            print(f"Erreur: Le nombre de passagers doit être entre 0 et {self.capacite_max}")


class Bus(VehiculeTransportPassagers):
    """Classe pour les bus"""
    
    def __init__(self, immatriculation, annee_achat, nb_passagers=0):
        """
        Constructeur de la classe Bus
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            nb_passagers (int, optional): Nombre de passagers. Defaults to 0.
        """
        super().__init__(immatriculation, annee_achat, 20, 50)  # 20 tonnes à vide, 50 passagers max
        self.setPassagers(nb_passagers)
    
    def vitesseMaximale(self):
        """Retourne la vitesse maximale du bus"""
        return 100  # 100 km/h tout le temps


class Taxi(VehiculeTransportPassagers):
    """Classe pour les taxis"""
    
    def __init__(self, immatriculation, annee_achat, nb_passagers=0):
        """
        Constructeur de la classe Taxi
        
        Args:
            immatriculation (str): Immatriculation du véhicule
            annee_achat (int): Année d'achat du véhicule
            nb_passagers (int, optional): Nombre de passagers. Defaults to 0.
        """
        super().__init__(immatriculation, annee_achat, 2, 4)  # 2 tonnes à vide, 4 passagers max
        self.setPassagers(nb_passagers)
    
    def vitesseMaximale(self):
        """Retourne la vitesse maximale du taxi"""
        return 130  # 130 km/h tout le temps
