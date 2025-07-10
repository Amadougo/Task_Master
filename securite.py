from data import EtatManip, Pression, Onduleur
from math import pow
from treatment import relais1_OFF, relais1_ON, relais2_OFF, relais2_ON
from treatment import pompe_SCU_1400_1_ON, pompe_SCU_1400_1_OFF, pompe_SCU_1400_2_ON, pompe_SCU_1400_2_OFF, pompe_SCU_800_OFF, pompe_SCU_800_ON
import subprocess
import time

PRESSION_SEUIL_PRIMAIRE = pow(10,-2) #milibar

def securite(etat_manip: EtatManip, pression: Pression, onduleur1 : Onduleur, onduleur2 : Onduleur) :
    
    print(f"{time.monotonic()}, passage dans la securite")
    print(f"onduleur2.battery_runtime = {onduleur2.battery_runtime}")
    
    #Actions lorsque la manip est en 'OFF'
    if (etat_manip == EtatManip.OFF) :
        print("État manip : 0FF")
        #print(f"seuil primaire défini à {PRESSION_SEUIL_PRIMAIRE}")
        #Exctinction de l'ordinateur en cas de coupure de courant prolongée
        if (int(onduleur2.battery_runtime) < 300) :  # 300 secondes = 5 minutes
            print("Coupure de courant prolongée, extinction de l'ordinateur")
            #Besoin des droits sudoers, à voir si on peut démarrer le programme avec les droits sudoers
            # ou bien si on peut désactiver les droits sudoers pour shutdown
            subprocess.run(["sudo", "shutdown", "-h", "now"])

    #Actions lorsque la manip est en 'Démarrage'
    elif (etat_manip == EtatManip.DEMARRAGE) :
        print("État manip : Démarrage…")
        #On démarre les pompes finales (relais)
        relais1_ON()
        relais2_ON()
        #On démarre les pompes secondaires
        pompe_SCU_1400_1_ON()
        pompe_SCU_1400_2_ON()
        pompe_SCU_800_ON()
        #On passe l'état de la manip à 'Fonctionnement'
        etat_manip = EtatManip.FONCTIONNE
        '''vérifier pompes primaires'''

    #Actions lorsque la manip est en 'Fonctionnement'
    elif (etat_manip == EtatManip.FONCTIONNE) :
        print("État manip : Fonctionne")

        #Première sécurité si la pression primaire est trop faible ou bien que la jauge est déconnectée
        if (pression.Jauge_5_Primaire == "Déconnectée" or pression.Jauge_5_Primaire == "Validation manuelle requise") :
            print("Erreur jauge primaire, arrêt des pompes")
            etat_manip = EtatManip.ARRET_EN_COURS
        else :
            value = pression.Jauge_5_Primaire.split(" ")      
            flt = float(value[0])
            if (flt > PRESSION_SEUIL_PRIMAIRE) :
                etat_manip = EtatManip.ARRET_EN_COURS
        #Deuxième sécurité en cas de coupure de courant de plus de 10min
        if (int(onduleur1.battery_runtime) < 240) :
            etat_manip = EtatManip.ARRET_EN_COURS
        

    #Actions lorsque la manip est en 'cours d'arrêt'
    elif (etat_manip == EtatManip.ARRET_EN_COURS) :
        print("État manip : Arrêt en cours")
        #On arrête les pompes finales (relais)
        relais1_OFF()
        relais2_OFF()
        #On arrête les pompes secondaires
        pompe_SCU_1400_1_OFF()
        pompe_SCU_1400_2_OFF()
        pompe_SCU_800_OFF()
        etat_manip = EtatManip.OFF
        

    print(f"{time.monotonic()}, fin du passage dans la securite")