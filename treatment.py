from data import Onduleur
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

#Fonction pour récupérer les données et les mettre dans la class 'Onduleur'
def recuperer_donnees_onduleur(onduleur : Onduleur) :
    ups_data = get_ups_data("onduleur@localhost")  # Remplace 'myups' par le nom exact de ton onduleur

    if ups_data:
        onduleur.input_voltage = ups_data.get("input.voltage", "Inconnue")
        onduleur.afficher_donnees_onduleur() # Affichage terminal optionnel
    else:
        print("Impossible de récupérer les données de l'onduleur.")
    
    return onduleur

    '''
    print("Fréquence d'entrée :", ups_data.get("input.frequency", "Inconnue"))
    print("Tension de batterie :", ups_data.get("battery.voltage", "Inconnue"))
    print("Autonomie estimée (en minutes) :", ups_data.get("battery.runtime", "Inconnue"))
    print("Chargement de la batterie :", ups_data.get("battery.charge", "Inconnue"), "%")
    print("Charge en sortie de l'onduleur :", ups_data.get("ups.load","Inconnue"),"%")
    print("Statut :", ups_data.get("ups.status", "Inconnu"))
    '''