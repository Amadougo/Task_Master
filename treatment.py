from data import Onduleur, Pression, Cathode, EtatCathode
import subprocess
import serial
import time
import math
from logs import * # type: ignore

#Fonction qui définie la récupération de données auprès de NUT
def get_ups_data(ups_name="onduleur1@localhost"):
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
    ups_data = get_ups_data(onduleur.name_ups_data) # Remplace 'myups' par le nom exact de ton onduleur
    
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
port_jauges = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_AWAFc143M08-if00-port0'
baud_rate = 9600
time_out = 1

serial_jauges = serial.Serial(port_jauges, baudrate= baud_rate, timeout=time_out)

if serial_jauges.is_open:
	print(f"port_jauges {port_jauges} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le port_jauges {port_jauges}")

#Port série pour les contrôleurs de pompes (SCU - 800, SCU - 1400 1 et 2)
port_SCU_800 = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_A_CRd143M08-if00-port0'
baud_rate = 9600
time_out = 1

serial_SCU_800 = serial.Serial(port_SCU_800, baudrate= baud_rate, timeout=time_out)

if serial_SCU_800.is_open:
	print(f"Port SCU 800 {port_SCU_800} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port_SCU_800}")

port_SCU_1400_1 = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_CGARc143M08-if00-port0'
baud_rate = 9600
time_out = 1

serial_SCU_1400_1 = serial.Serial(port_SCU_1400_1, baudrate= baud_rate, timeout=time_out)

if serial_SCU_1400_1.is_open:
	print(f"Port SCU 1400 1 {port_SCU_1400_1} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port_SCU_1400_1}")

port_SCU_1400_2 = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller_EDAQc143M08-if00-port0'
baud_rate = 9600
time_out = 1

serial_SCU_1400_2 = serial.Serial(port_SCU_1400_2, baudrate= baud_rate, timeout=time_out)

if serial_SCU_1400_2.is_open:
	print(f"Port SCU 1400 2 {port_SCU_1400_2} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port_SCU_1400_2}")

#Port série pour le contrôleur de cathode
port_cathode = '/dev/serial/by-id/usb-Prolific_Technology_Inc._ATEN_USB_to_Serial_Bridge-if00-port0'
baud_rate = 9600
time_out = 1

serial_cathode = serial.Serial(port_cathode, baudrate= baud_rate, timeout=time_out)

if serial_cathode.is_open:
	print(f"Port {port_cathode} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port_cathode}")

#Port série pour la sécurité des pompes finales
port_secu_finale = '/dev/ttyS0'
baud_rate = 19200
time_out = 1

serial_secu_finale = serial.Serial(port_secu_finale, baudrate= baud_rate, timeout=time_out)

if serial_secu_finale.is_open:
	print(f"Port {port_secu_finale} ouvert avec succès.")
else:
	print(f"Impossible d'ouvrir le Port {port_secu_finale}")
     
#Fonction périodique

def recuperer_donnees_pression_jauge1(pression : Pression) : #913, 914, 915, 934, 935, 936
    #Cette commande renvoie les valeurs de toutes les jauges
    command = "?V913\r"
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    serial_jauges.write(command.encode())
    response = serial_jauges.readline().decode().strip()
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
    #Récupération du courant
    command = "I?\n"
    serial_cathode.write(command.encode())
    response = serial_cathode.readline().decode().strip()
    print(f"reponse = {response}")
    if(response == '' or response[0] != "I"):
       cathode.etat = EtatCathode.DECONNECTEE
    elif(cathode.etat == EtatCathode.DECONNECTEE):
        cathode.etat = EtatCathode.FROIDE # Seulement pour la première où l'appareil est reconnecté/rallumé

    #
    print(f"état de la cathode : {cathode.etat}")
    #

    if(cathode.etat != EtatCathode.DECONNECTEE):
        #Convertion du temps en secondes
        consigne_temps_seconde = cathode.consigne_temps*60
        
        #Récupération du courant
        command = "I?\n"
        serial_cathode.write(command.encode())
        response = serial_cathode.readline().decode().strip()
        courant_cathode = float(response[len("I "):])
        print(f"Le courant est : {courant_cathode}A")

        #Récupération de la tension
        command = "V?\n"
        serial_cathode.write(command.encode())
        response = serial_cathode.readline().decode().strip()
        tension_cathode = float(response[len("V "):])
        print(f"La tension est : {tension_cathode}V")
        
        if tension_cathode != 18.00 :
            command = "V 18.00\n"
            serial_cathode.write(command.encode())

        if cathode.etat == EtatCathode.CHAUFFE : 
            #Calcul du temps ecoulé
            t_ecoule = time.monotonic() - cathode.t_0
            print(f"temps écoulé = {t_ecoule}")
            #Test si fini
            if (courant_cathode > cathode.consigne_courant) or (t_ecoule > consigne_temps_seconde) :
                cathode.etat = EtatCathode.CHAUDE
                log_with_cooldown(logging.INFO, "Chauffe de la cathode terminee.")
                return
            #Calcul de la fonction
            intensite_cathode = math.sqrt(t_ecoule/(consigne_temps_seconde/math.pow(cathode.consigne_courant,2)))
            #Mise Ã  jour du courant
            command = "I " + str(intensite_cathode) + "\n"
            print(f" commande envoyée : {command}")
            serial_cathode.write(command.encode())

        if cathode.etat == EtatCathode.REFROIDISSEMENT : 
            #Calcul du temps écoulé
            t_ecoule = consigne_temps_seconde - time.monotonic() - cathode.t_0
            #Test si fini
            if (courant_cathode <= cathode.consigne_courant) or (t_ecoule <= 0) :
                cathode.etat = EtatCathode.FROIDE
                log_with_cooldown(logging.INFO, "Refroidissement de la cathode terminee.")
                return
            #Calcul de la fonction
            intensite_cathode = math.sqrt(t_ecoule/(consigne_temps_seconde/math.pow(cathode.consigne_courant,2)))
            #Mise à jour du courant
            command = "I " + str(intensite_cathode) + "\n"
            print(f" commande envoyée : {command}")
            serial_cathode.write(command.encode())

# -------------------------------- #
#  Gestion des pompes secondaires  #
# -------------------------------- #

def envoyer_commande_SCU_800(cmd_bytes):
    print(f"Envoi : {cmd_bytes.hex()}")
    serial_SCU_800.write(cmd_bytes)
    time.sleep(0.2)  # Laisse un peu le temps à la réponse d'arriver
    response = serial_SCU_800.read(100)
    print("Réponse brute hex :", response.hex())
    try:
        print("Réponse ASCII :", response.decode('ascii', errors='replace'))
    except:
        print("Impossible de décoder la réponse.")

def pompe_SCU_800_ON():
    # Commande allumer pompe SCU-800
    cmd_on =  bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x31, 0x03, 0xAB]) # E1 SetPORT : Pompe SCU-800 allumée
    envoyer_commande_SCU_800(cmd_on)

def pompe_SCU_800_OFF():
    # Commande éteindre pompe SCU-800
    cmd_off = bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x32, 0x03, 0xA8]) # E2 brake SetPORT : Pompe SCU-800 éteinte
    envoyer_commande_SCU_800(cmd_off)

def recuperer_etat_SCU_800():
    cmd_bytes = bytes([0x02, 0x30, 0x30, 0x31, 0x3F, 0x4D, 0x03, 0xBD]) #?M
    
    print(f"Envoi : {cmd_bytes.hex()}")
    serial_SCU_800.write(cmd_bytes)
    time.sleep(0.2)  # Laisse un peu le temps à la réponse d'arriver
    responseSCU800 = serial_SCU_800.read(100)
    print("Réponse brute hex :", responseSCU800.hex())
    try:
        print("Réponse ASCII :", responseSCU800.decode('ascii', errors='replace'))
    except:
        print("Impossible de décoder la réponse.")
    
    return responseSCU800[3]

def envoyer_commande_SCU_1400_1(cmd_bytes):
    print(f"Envoi : {cmd_bytes.hex()}")
    serial_SCU_1400_1.write(cmd_bytes)
    time.sleep(0.2)  # Laisse un peu le temps à la réponse d'arriver
    response = serial_SCU_1400_1.read(100)
    print("Réponse brute hex :", response.hex())
    try:
        print("Réponse ASCII :", response.decode('ascii', errors='replace'))
    except:
        print("Impossible de décoder la réponse.")

def pompe_SCU_1400_1_ON():
    # Commande allumer pompe SCU-1400 1
    cmd_on =  bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x31, 0x03, 0xAB]) # E1 SetPORT : Pompe SCU-1400 1 allumée
    envoyer_commande_SCU_1400_1(cmd_on)

def pompe_SCU_1400_1_OFF():
    # Commande éteindre pompe SCU-1400 1
    cmd_off = bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x32, 0x03, 0xA8]) # E2 brake SetPORT : Pompe SCU-1400 1 éteinte
    envoyer_commande_SCU_1400_1(cmd_off)

def envoyer_commande_SCU_1400_2(cmd_bytes):
    print(f"Envoi : {cmd_bytes.hex()}")
    serial_SCU_1400_2.write(cmd_bytes)
    time.sleep(0.2)  # Laisse un peu le temps à la réponse d'arriver
    response = serial_SCU_1400_2.read(100)
    print("Réponse brute hex :", response.hex())
    try:
        print("Réponse ASCII :", response.decode('ascii', errors='replace'))
    except:
        print("Impossible de décoder la réponse.")

def pompe_SCU_1400_2_ON():
    # Commande allumer pompe SCU-1400 2
    cmd_on =  bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x31, 0x03, 0xAB]) # E1 SetPORT : Pompe SCU-1400 2 allumée
    envoyer_commande_SCU_1400_2(cmd_on)

def pompe_SCU_1400_2_OFF():
    # Commande éteindre pompe SCU-1400 2
    cmd_off = bytes([0x02, 0x30, 0x30, 0x31, 0x20, 0x45, 0x30, 0x32, 0x03, 0xA8]) # E2 brake SetPORT : Pompe SCU-1400 2 éteinte
    envoyer_commande_SCU_1400_2(cmd_off)

# -------------------------------- #
#    Gestion de la carte relais    #
# -------------------------------- #
    
def envoyer_commande_carte_relais(cmd_bytes):
    print(f"Envoi : {cmd_bytes.hex()}")
    serial_secu_finale.write(cmd_bytes)
    time.sleep(0.2)  # Laisse un peu le temps à la réponse d'arriver
    response = serial_secu_finale.read(100)
    print("Réponse brute hex :", response.hex())
    try:
        print("Réponse ASCII :", response.decode('ascii', errors='replace'))
    except:
        print("Impossible de décoder la réponse.")

def relais1et2_OFF():
    # IMPORTANT : Initialisé au moins au démarrage de la carte de commande des relais
    cmd_init = bytes([0x01, 0x01, 0x00, 0x00]) # Initialisation
    envoyer_commande_carte_relais(cmd_init)
    
    # Attendre 1 seconde
    time.sleep(1)

    # Commande éteindre relais 1 et 2
    cmd_off = bytes([0x03, 0x01, 0x00, 0x02]) # SetPORT : Relais1 éteint
    envoyer_commande_carte_relais(cmd_off)

def relais1et2_ON():
    # IMPORTANT  Initialisé au moins au démarrage de la carte de commande des relais
    cmd_init = bytes([0x01, 0x01, 0x00, 0x00]) # Initialisation
    envoyer_commande_carte_relais(cmd_init)
    
    # Attendre 1 seconde
    time.sleep(1)
    
    # Commande allumer relais 1 et 2
    cmd_on = bytes([0x03, 0x01, 0x03, 0x01]) # SetPORT  Relais1 allumé
    envoyer_commande_carte_relais(cmd_on)








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