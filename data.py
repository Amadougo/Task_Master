print("Chargement de data.py\n")

class Onduleur :
    def __init__(
        self,
        input_voltage: int = 0,
        input_frequency: float = 0.0,
        battery_voltage: float = 0.0,
        battery_runtime: int = 0,
        battery_charge: int = 0,
        ups_load: int = 0,
        ups_status: str = ""
    ):
        self.input_voltage = input_voltage
        self.input_frequency = input_frequency
        self.battery_voltage = battery_voltage
        self.battery_runtime = battery_runtime
        self.battery_charge = battery_charge
        self.ups_load = ups_load
        self.ups_status = ups_status

    def afficher_donnees_onduleur(self):
        print(f"Tension d'entrée : {self.input_voltage} V")
        print(f"Fréquence d'entrée : {self.input_frequency} Hz")
        print(f"Tension de batterie : {self.battery_voltage} V")
        print(f"Autonomie estimée (en secondes) :{self.battery_runtime} s")
        print(f"Chargement de la batterie :{self.battery_charge} %")
        print(f"Charge en sortie de l'onduleur : {self.ups_load} %")
        print(f"Statut : {self.ups_status}")

class Pression :
    def __init__(
        self,
        Jauge_1_Turbo: str = "Déconnectée",
        Jauge_2_Turbo: str = "Déconnectée",
        Jauge_3_Turbo: str = "Déconnectée",
        Jauge_4_Turbo: str = "Déconnectée",
        Jauge_5_Primaire: str = "Déconnectée",
        Jauge_6_Vide: str = "Déconnectée",
    ):
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

