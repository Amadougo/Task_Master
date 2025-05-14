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
        print(f"Fréquence d'entrée :", {self.input_frequency}, "Hz")
        print(f"Tension de batterie :", {self.battery_voltage}, "V")
        print(f"Autonomie estimée (en secondes) :",{self.battery_runtime}, "s")
        print(f"Chargement de la batterie :",{self.battery_charge}, "%")
        print(f"Charge en sortie de l'onduleur :", {self.ups_load},"%")
        print(f"Statut :", {self.ups_status})

