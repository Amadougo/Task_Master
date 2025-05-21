from data import Onduleur, Pression
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1
from GUI import Gui # import the GUI class from GUI.py

# Onduleur
onduleur = Onduleur()
recuperer_donnees_onduleur(onduleur)

# Pression
pression = Pression()
recuperer_donnees_pression_jauge1(pression)

# Creation of the GUI
gui = Gui(onduleur, pression)

# Rescale images
gui.resize_images()

# Run the user interface
gui.run()