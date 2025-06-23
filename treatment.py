from data import Onduleur, Pression, Cathode, EtatCathode
import subprocess
import serial
import time
import math

#Variables globales
t_0 = 0.0 # = time.clock_gettime(time.CLOCK_MONOTONIC)

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
        #onduleur.afficher_donnees_onduleur() 
    else:
        print("Impossible de récupérer les données de l'onduleur.")
    
    return onduleur

#Fonctions pour récupérer les données de pression et les mettre dans la class 'Pression'
#Récupérations globales
#Port série pour les jauges de pression
port = '/dev/serial/by-id/usb-Prolific_Technology_Inc._ATEN_USB_to_Serial_Bridge-if00-port0'
baud_rate = 9600
time_out = 1

ser = serial.Serial(port, baudrate= baud_rate, timeout=time_out)

if ser.is_open:
	print(f"Port {port} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port}")

#Port série pour les contrôleurs de pompes (SCU - 800, SCU - 1400 x2)
'''port2 = '/dev/serial/by-id/usb-Prolific_Technology_Inc._ATEN_USB_to_Serial_Bridge-if00-port1'
baud_rate = 9600
time_out = 1

ser2 = serial.Serial(port2, baudrate= baud_rate, timeout=time_out)

if ser2.is_open:
	print(f"Port {port2} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port2}")'''
     
#Fonction périodique

def recuperer_donnees_pression_jauge1(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V913\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V913 "):
        data_str = response[len("=V913 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_1_Turbo = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_1_Turbo = 'Validation manuelle requise'        
        else :
            pression.Jauge_1_Turbo = 'Déconnectée'
    return Pression

def recuperer_donnees_pression_jauge2(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V914\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V914 "):
        data_str = response[len("=V914 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_2_Turbo = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_2_Turbo = 'Validation manuelle requise'        
        else :
            pression.Jauge_2_Turbo = 'Déconnectée'
    return Pression

def recuperer_donnees_pression_jauge3(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V915\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V915 "):
        data_str = response[len("=V915 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_3_Turbo = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_3_Turbo = 'Validation manuelle requise'        
        else :
            pression.Jauge_3_Turbo = 'Déconnectée'
    return Pression

def recuperer_donnees_pression_jauge4(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de 1 jauge
    command = "?V934\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V934 "):
        data_str = response[len("=V934 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_4_Turbo = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_4_Turbo = 'Validation manuelle requise'        
        else :
            pression.Jauge_4_Turbo = 'Déconnectée'
    return Pression

def recuperer_donnees_pression_jauge5(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V935\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V935 "):
        data_str = response[len("=V935 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_5_Primaire = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_5_Primaire = 'Validation manuelle requise'        
        else :
            pression.Jauge_5_Primaire = 'Déconnectée'
    return Pression

def recuperer_donnees_pression_jauge6(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V936\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V936 "):
        data_str = response[len("=V936 "):]

    # 2. Séparer par les points-virgules
        values = data_str.split(";")
        
    # 3. Vérifier le statut de la jauge
        if (values[2] == '11') :
            pression.Jauge_6_Vide = f"{float(values[0]) * 0.00750062:.2e} Torr"
    # 4. enregistrer la valeur lue
        elif values[2] == '2' :
            pression.Jauge_6_Vide = 'Validation manuelle requise'        
        else :
            pression.Jauge_6_Vide = 'Déconnectée'
    return Pression

def controle_cathode(cathode: Cathode):

    #Récupration du courant
    command = "I?\n"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    courant_cathode = float(response[len("I "):])
    print(f"Le courant est : {courant_cathode}A")

    #Récupration de la tension
    command = "V?\n"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    tension_cathode = float(response[len("V "):])
    print(f"La tension est : {tension_cathode}V")
    
    if tension_cathode != 18.00 :
        command = "V 18.00\n"
        ser.write(command.encode())

    if cathode.etat == EtatCathode.CHAUFFE : 
        #Calcul du temps ecoulÃ©
        t_ecoule = time.clock_gettime(time.CLOCK_MONOTONIC) - t_0
        print(f"temps écoulé = {t_ecoule}")
        #Test si fini
        if (courant_cathode > 8.00) or (t_ecoule > 2700) :
            cathode.etat = EtatCathode.CHAUDE
            return
        #Calcul de la fonction
        intensite_cathode = math.sqrt(t_ecoule/42.1875)
        #Mise Ã  jour du courant
        command = "I " + str(intensite_cathode) + "\n"
        print(f" commande envoyée : {command}")
        ser.write(command.encode())

    if cathode.etat == EtatCathode.REFROIDISSEMENT : 
        #Calcul du temps écoulé
        t_ecoule = 2700 - time.clock_gettime(time.CLOCK_MONOTONIC) - t_0
        #Test si fini
        if (courant_cathode <= 0.38) or (t_ecoule <= 0) :
            cathode.etat = EtatCathode.FROIDE
            return
        #Calcul de la fonction
        intensite_cathode = math.sqrt(t_ecoule/42.1875)
        #Mise à jour du courant
        command = "I " + str(intensite_cathode) + "\n"
        print(f" commande envoyée : {command}")
        ser.write(command.encode())
    










'''
def recuperer_donnees_pression(pression : Pression) :
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V940\r"
    ser.write(command.encode())
    response = ser.readline().decode().strip()
    # 1. Enlever le préfixe (facultatif)
    if response.startswith("=V940 "):
        data_str = response[len("=V940 "):]

        # 2. Séparer par les points-virgules
        values = data_str.split(";")

        i = 0
        #while i < len(values):
        # 3. Vérifier le statut de la jauge
        if (values[i] == '1') and (i < len(values)):
            # 4. enregistrer la valeur lue
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_1_Turbo = 'OFF'
            else :
                pression.Jauge_1_Turbo = values[i] + "Torr"
            i+=2
        else :
            pression.Jauge_1_Turbo = 'Déconnectée'
        
        if (values[i] == '2') and (i < len(values)):
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_2_Turbo = 'OFF'
            else :
                pression.Jauge_2_Turbo = values[i]+ "Torr"
            i+=2
        else :
            pression.Jauge_2_Turbo = 'Déconnectée'

        if (values[i] == '3') and (i < len(values)):
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_3_Turbo = 'OFF'
            else :
                pression.Jauge_3_Turbo = values[i]+ "Torr"
            i+=2
        else :
            pression.Jauge_3_Turbo = 'Déconnectée'

        if (values[i] == '4') and (i < len(values)):
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_4_Turbo = 'OFF'
            else :
                pression.Jauge_4_Turbo = values[i]+ "Torr"
            i+=2
        else :
            pression.Jauge_4_Turbo = 'Déconnectée'

        if (values[i] == '5') and (i < len(values)):
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_5_Primaire = 'OFF'
            else :
                pression.Jauge_5_Primaire = values[i]+ "Torr"
            i+=2
        else :
            pression.Jauge_5_Primaire = 'Déconnectée'

        if (values[i] == '6') and (i < len(values)):
            if values[i+1] == '9.9000e+09' :
                pression.Jauge_6_Vide = 'OFF'
            else :
                pression.Jauge_6_Vide = values[i]+ "Torr"
            i+=2
        else :
            pression.Jauge_6_Vide = 'Déconnectée'

    else:
        print("Erreur lors de la récupération des valeurs de jauge.")

    return pression
'''