from data import EtatManip, Pression, Onduleur
from math import pow
from treatment import relais1et2_OFF, relais1et2_ON
from treatment import pompe_SCU_1400_1_ON, pompe_SCU_1400_1_OFF, pompe_SCU_1400_2_ON, pompe_SCU_1400_2_OFF, pompe_SCU_800_OFF, pompe_SCU_800_ON
from treatment import recuperer_etat_SCU_800
import subprocess
import time
from logs import * # type: ignore

PRESSION_SEUIL_PRIMAIRE = 7.1*pow(10,-3) #Torr
class Securite:
    def __init__(self, etat_manip, pression, onduleur1, onduleur2, securite_pression_actif):
        self.etat_manip = etat_manip
        self.pression = pression
        self.onduleur1 = onduleur1
        self.onduleur2 = onduleur2
        self.securite_pression_actif = securite_pression_actif  # Indicateur pour activer ou désactiver la sécurité

    def securite(self) :
        print(f"PRESSION_SEUIL_PRIMAIRE = {PRESSION_SEUIL_PRIMAIRE}")
        #Actions lorsque la manip est en 'OFF'
        if (self.etat_manip == EtatManip.OFF) :
            """#Exctinction de l'ordinateur en cas de coupure de courant prolongée
            if (int(self.onduleur2.battery_runtime) < 300) :  # 300 secondes = 5 minutes
                print("Coupure de courant prolongée, extinction de l'ordinateur")
                #Besoin des droits sudoers, à voir si on peut démarrer le programme avec les droits sudoers
                # ou bien si on peut désactiver les droits sudoers pour shutdown
                subprocess.run(["sudo", "shutdown", "-h", "now"])"""

        #Actions lorsque la manip est en 'Démarrage'
        elif (self.etat_manip == EtatManip.DEMARRAGE) :
            etat_SCU = recuperer_etat_SCU_800()
            if (etat_SCU == 1 or etat_SCU == 5):
                #On démarre les pompes finales (relais)
                relais1et2_ON()
                #On démarre les pompes secondaires
                pompe_SCU_1400_1_ON()
                pompe_SCU_1400_2_ON()
                pompe_SCU_800_ON()
            elif(etat_SCU == 4):
                #On passe l'état de la manip à 'Fonctionnement'
                self.etat_manip = EtatManip.FONCTIONNE
            elif(etat_SCU != 3):
                #Démarrage impossible
                log_with_cooldown(logging.CRITICAL, "Erreur SCU800 lors du démarrage de la manipulation")
            time.sleep(5)  # Attente pour éviter une boucle trop rapide             

        #Actions lorsque la manip est en 'Fonctionnement'
        elif (self.etat_manip == EtatManip.FONCTIONNE) :
            #On vérifie si la sécurité de pression est active
            if self.securite_pression_actif:
                #Première sécurité si la pression primaire est trop faible ou bien que la jauge est déconnectée
                if (self.pression.Jauge_5_Primaire == "Déconnectée" or self.pression.Jauge_5_Primaire == "Validation manuelle requise") :
                    self.etat_manip = EtatManip.ARRET_EN_COURS
                    log_with_cooldown(logging.CRITICAL, "Erreur jauge primaire -> arrêt de la manipulation")
                else :
                    value = self.pression.Jauge_5_Primaire.split(" ")      
                    flt = float(value[0])
                    if (flt > PRESSION_SEUIL_PRIMAIRE) :
                        self.etat_manip = EtatManip.ARRET_EN_COURS
                        log_with_cooldown(logging.CRITICAL, f"La jauge de pression 5 a depasse la valeur seuil de {PRESSION_SEUIL_PRIMAIRE} Torr.")
            #Deuxième sécurité en cas de coupure de courant de plus de 10min
            #La manipe se coupe lorsqu'il reste moins de 240 secondes = 4 minutes
            # d'autonomie sur l'onduleur1
            if (int(self.onduleur1.battery_runtime) < 240) :
                self.etat_manip = EtatManip.ARRET_EN_COURS
                log_with_cooldown(logging.CRITICAL, "Arret general pour cause onduleur1 presque vide (4 minutes restantes avant batteries vides).")
            

        #Actions lorsque la manip est en 'cours d'arrêt'
        elif (self.etat_manip == EtatManip.ARRET_EN_COURS) :
            etat_SCU = recuperer_etat_SCU_800()
            if (etat_SCU == 4 or etat_SCU == 3):
                #On arrête les pompes finales (relais)
                relais1et2_OFF()
                #On arrête les pompes secondaires
                pompe_SCU_1400_1_OFF()
                pompe_SCU_1400_2_OFF()
                pompe_SCU_800_OFF()
            elif(etat_SCU == 1):
                #On passe l'état de la manip à 'OFF'
                self.etat_manip = EtatManip.OFF
            elif(etat_SCU != 5):
                #Arrêt impossible
                log_with_cooldown(logging.CRITICAL, "Erreur SCU800 lors de l'arrêt de la manipulation")
            time.sleep(5)  # Attente pour éviter une boucle trop rapide