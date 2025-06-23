from data import Onduleur, Pression, Cathode
#from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
from GUI import Gui # import the GUI class from GUI.py

# Creation of an Onduleur object
onduleur = Onduleur()

# Creation of a Pression object
pression = Pression()

# Creation of a Cathode object
cathode = Cathode()

# Creation of the GUI
gui = Gui(onduleur, pression, cathode, affichage_donnees=True)

# Get Onduleur and Pression data
#gui.recuperer_donnees(onduleur, pression)

"""# Rescale images
#gui.resize_images()"""

# Force the resize of boxes dimensions
gui.force_initial_resizing()

# Run the user interface
gui.run()