from data import Onduleur
from treatment import recuperer_donnees_onduleur
from GUI import Gui # import the GUI class from GUI.py

onduleur = Onduleur()
recuperer_donnees_onduleur(onduleur)

# Creation of the GUI
gui = Gui(onduleur)

# Run the user interface
gui.run()