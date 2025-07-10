from data import Onduleur, Pression, Cathode, EtatManip
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
import os
import time
import threading 
from securite import Securite

# Creation of an Onduleur object
onduleur1 = Onduleur()

onduleur2 = Onduleur()

# Creation of a Pression object
pression = Pression()

# Creation of a Cathode object
cathode = Cathode()

# Creation of a EtatManip object
etatManip: EtatManip = EtatManip.OFF

# Creation of a Securite object
securite = Securite(etatManip, pression, onduleur1, onduleur2)

while(os.environ.get("DISPLAY") == None):
    recuperer_donnees_onduleur(onduleur1)
    recuperer_donnees_onduleur(onduleur2)
    recuperer_donnees_pression_jauge1(pression)
    recuperer_donnees_pression_jauge2(pression)
    recuperer_donnees_pression_jauge3(pression)
    recuperer_donnees_pression_jauge4(pression)
    recuperer_donnees_pression_jauge5(pression)
    recuperer_donnees_pression_jauge6(pression)
    securite.securite()
    print("test OS")
    time.sleep(1)

from GUI import Gui # import the GUI class from GUI.py

print("interface graphique")

# Creation of the GUI
gui = Gui(onduleur1, onduleur2, pression, cathode, etatManip, securite, affichage_donnees=True, mode_securite_actif=True)

# Force the resize of boxes dimensions
gui.force_initial_resizing()

# Run the user interface
gui.run()