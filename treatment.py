from data import Onduleur, Pression
import subprocess

#Fonction qui définie la récupération de données auprès de NUT
def get_ups_data(ups_name="onduleur@localhost"):
    try:
        # Lance la commande 'upsc'
        result = subprocess.run(["upsc", ups_name], capture_output=True, text=True, check=True)
        data_lines = result.stdout.strip().split("\n")
        
        # Convertit chaque ligne en dictionnaire clé:valeur
        data = {}
        for line in data_lines:
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        return data

    except subprocess.CalledProcessError as e:
        print("Erreur avec upsc :", e)
        return None
    except FileNotFoundError:
        print("La commande 'upsc' n'est pas trouvée. Vérifie que NUT est installé.")
        return None

#Fonction pour récupérer les données de l'onduleur et les mettre dans la class 'Onduleur'
def recuperer_donnees_onduleur(onduleur : Onduleur) :
    ups_data = get_ups_data("onduleur@localhost")  # Remplace 'myups' par le nom exact de ton onduleur

    if ups_data:
        onduleur.input_voltage = ups_data.get("input.voltage", "Inconnue")
        onduleur.input_frequency = ups_data.get("input.frequency", "Inconnue")
        onduleur.battery_voltage = ups_data.get("battery.voltage", "Inconnue")
        onduleur.battery_runtime = ups_data.get("battery.runtime", "Inconnue")
        onduleur.battery_charge = ups_data.get("battery.charge", "Inconnue")
        onduleur.ups_load = ups_data.get("ups.load","Inconnue")
        onduleur.ups_status = ups_data.get("ups.status", "Inconnu")
        # Affichage terminal optionnel
        onduleur.afficher_donnees_onduleur() 
    else:
        print("Impossible de récupérer les données de l'onduleur.")
    
    return onduleur

#Fonction pour récupérer les données de pression et les mettre dans la class 'Pression'

def recuperer_donnees_pression(pression : Pression) :
    #o
    return 