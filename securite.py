from data import EtatManip, Pression
from math import pow

PRESSION_SEUIL_PRIMAIRE = pow(10,-2) #milibar

def securite(etat_manip: EtatManip, pression: Pression ) :
    #Actions lorsque la manip est en 'OFF'
    if (etat_manip == EtatManip.OFF) :
        print("État manip : 0FF")
        #print(f"seuil primaire défini à {PRESSION_SEUIL_PRIMAIRE}")

    #Actions lorsque la manip est en 'Démarrage'
    elif (etat_manip == EtatManip.DEMARRAGE) :
        print("État manip : Démarrage…")

    #Actions lorsque la manip est en 'Fonctionnement'
    elif (etat_manip == EtatManip.FONCTIONNE) :
        print("État manip : Fonctionne")
        if (pression.Jauge_5_Primaire == "Déconnectée" or pression.Jauge_5_Primaire == "Validation manuelle requise") :
            print("Erreur jauge primaire, arrêt des pompes")
            etat_manip = EtatManip.ARRET_EN_COURS
        else :
            value = pression.Jauge_5_Primaire.split(" ")      
            flt = float(value[0])
            if (flt > PRESSION_SEUIL_PRIMAIRE) :
                etat_manip = EtatManip.ARRET_EN_COURS

    #Actions lorsque la manip est en 'cours d'arrêt'
    elif (etat_manip == EtatManip.ARRET_EN_COURS) :
        print("État manip : Arrêt en cours")

etat_manip: EtatManip = EtatManip.OFF
pression = Pression()
securite(etat_manip, pression)    