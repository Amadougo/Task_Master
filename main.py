from data import Onduleur, Pression
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
from GUI import Gui # import the GUI class from GUI.py

# Onduleur
onduleur = Onduleur()
recuperer_donnees_onduleur(onduleur)

# Pression
pression = Pression()
recuperer_donnees_pression_jauge1(pression)
recuperer_donnees_pression_jauge2(pression)
recuperer_donnees_pression_jauge3(pression)
recuperer_donnees_pression_jauge4(pression)
recuperer_donnees_pression_jauge5(pression)
recuperer_donnees_pression_jauge6(pression)

# Creation of the GUI
gui = Gui(onduleur, pression)

# Rescale images
gui.resize_images()

# Run the user interface
gui.run()