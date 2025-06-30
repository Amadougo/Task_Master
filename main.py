from data import Onduleur, Pression, Cathode, EtatManip
#from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
from GUI import Gui # import the GUI class from GUI.py
import os
import time
#from securite import securite

# Creation of an Onduleur object
onduleur1 = Onduleur()

onduleur2 = Onduleur()

# Creation of a Pression object
pression = Pression()

# Creation of a Cathode object
cathode = Cathode()

# Creation of a EtatManip object
etatManip: EtatManip = EtatManip.OFF

print(f"{os.environ.get("DISPLAY")} = ")
while(os.environ.get("DISPLAY") == None):
    # recuperer_donnees_onduleur(onduleur1)
    # recuperer_donnees_onduleur(onduleur2)
    # recuperer_donnees_pression_jauge1(pression)
    # recuperer_donnees_pression_jauge2(pression)
    # recuperer_donnees_pression_jauge3(pression)
    # recuperer_donnees_pression_jauge4(pression)
    # recuperer_donnees_pression_jauge5(pression)
    # recuperer_donnees_pression_jauge6(pression)
    #securite(etatManip, pression, onduleur1, onduleur2)
    time.sleep(1)

# Creation of the GUI
gui = Gui(onduleur1, onduleur2, pression, cathode, etatManip, affichage_donnees=True, mode_securite_actif=True)

# Get Onduleur and Pression data
#gui.recuperer_donnees(onduleur, pression)

"""# Rescale images
#gui.resize_images()"""

# Force the resize of boxes dimensions
gui.force_initial_resizing()

# Run the user interface
gui.run()