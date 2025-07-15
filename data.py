print("Chargement de data.py\n")
# Définition du type énuméré EtatCathode
from enum import Enum

class Onduleur :
    def __init__(self,
                 input_voltage: int = 0,
                 input_frequency: float = 0.0,
                 battery_voltage: float = 0.0,
                 battery_runtime: int = 0,
                 battery_charge: int = 0,
                 ups_load: int = 0,
                 ups_status: str = "", 
                 name_ups_data: str = ""):
        self.input_voltage = input_voltage
        self.input_frequency = input_frequency
        self.battery_voltage = battery_voltage
        self.battery_runtime = battery_runtime
        self.battery_charge = battery_charge
        self.ups_load = ups_load
        self.ups_status = ups_status
        self.name_ups_data = name_ups_data

    def afficher_donnees_onduleur(self):
        print(f"Tension d'entrée : {self.input_voltage} V")
        print(f"Fréquence d'entrée : {self.input_frequency} Hz")
        print(f"Tension de batterie : {self.battery_voltage} V")
        print(f"Autonomie estimée (en secondes) :{self.battery_runtime} s")
        print(f"Chargement de la batterie :{self.battery_charge} %")
        print(f"Charge en sortie de l'onduleur : {self.ups_load} %")
        print(f"Statut : {self.ups_status}")

class Pression :
    def __init__(self,
                 Jauge_1_Turbo: str = "Déconnectée",
                 Jauge_2_Turbo: str = "Déconnectée",
                 Jauge_3_Turbo: str = "Déconnectée",
                 Jauge_4_Turbo: str = "Déconnectée",
                 Jauge_5_Primaire: str = "Déconnectée",
                 Jauge_6_Vide: str = "Déconnectée"):
        self.Jauge_1_Turbo = Jauge_1_Turbo
        self.Jauge_2_Turbo = Jauge_2_Turbo
        self.Jauge_3_Turbo = Jauge_3_Turbo
        self.Jauge_4_Turbo = Jauge_4_Turbo
        self.Jauge_5_Primaire = Jauge_5_Primaire
        self.Jauge_6_Vide = Jauge_6_Vide

    def afficher_donnees_pression(self):
        print(f"Jauge 1 : {self.Jauge_1_Turbo} ")
        print(f"Jauge 2 : {self.Jauge_2_Turbo} ")
        print(f"Jauge 3 : {self.Jauge_3_Turbo} ")
        print(f"Jauge 4 : {self.Jauge_4_Turbo} ")
        print(f"Jauge 5 Pompe primaire : {self.Jauge_5_Primaire} ")
        print(f"Jauge 6 Pompe non connectée : {self.Jauge_6_Vide} ")

class EtatCathode(Enum):
    FROIDE = "froide"
    CHAUFFE = "chauffe"
    CHAUDE = "chaude"
    REFROIDISSEMENT = "refroidissement"
    DECONNECTEE = "deconnectee"

class Cathode:
    def __init__(self,
                 etat: EtatCathode = EtatCathode.FROIDE,
                 t_0: float = 0.0,
                 tension: float = 0.0,
                 courant: float = 0.0,
                 consigne_courant: float = 0.0,
                 consigne_temps: int = 0):
        self.etat = etat
        self.t_0 = t_0
        self.tension = tension
        self.courant = courant
        self.consigne_courant = consigne_courant
        self.consigne_temps = consigne_temps

    def afficher_donnees(self):
        print(f"État de la cathode : {self.etat.value}")
        print(f"Tension : {self.tension} V")
        print(f"Courant : {self.courant} A")

class EtatManip(Enum):
    OFF = "off"
    DEMARRAGE = "demarrage"
    FONCTIONNE = "fonctionne"
    ARRET_EN_COURS = "arret en cours"
