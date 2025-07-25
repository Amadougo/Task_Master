from data import Onduleur, Pression, Cathode, EtatManip, CoupureCourant
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
import os
import time
from securite import Securite
from logs import * # type: ignore
import subprocess

# Creation of an Onduleur object
onduleur1 = Onduleur(name_ups_data="onduleur1@localhost")

onduleur2 = Onduleur(name_ups_data="onduleur2@localhost")

# Creation of a Pression object
pression = Pression()

# Creation of a Cathode object
cathode = Cathode()

# Creation of a EtatManip object
etatManip: EtatManip = EtatManip.OFF

# Creation of a CoupureCourant object
coupureCourant = CoupureCourant()

# Creation of a Securite object
est_securite_active = True
securite = Securite(etatManip, pression, onduleur1, onduleur2, coupureCourant, est_securite_active)

log_with_cooldown(logging.INFO, "Démarrage du programme",60)
# subprocess.run(["sudo", "upsdrvctl", "start"]) # Lancement driver onduleur en cas de coupure de courant

"""while(os.environ.get("DISPLAY") is None or os.environ.get("WAYLAND_DISPLAY") is None):
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
    time.sleep(1)"""

time.sleep(15)

from GUI import Gui # import the GUI class from GUI.py

print("interface graphique")

# Creation of the GUI
gui = Gui(onduleur1, onduleur2, pression, cathode, etatManip, securite, coupureCourant, affichage_donnees=True, mode_securite_actif=est_securite_active)

# Force the resize of boxes dimensions
gui.force_initial_resizing()

# Run the user interface
gui.run()