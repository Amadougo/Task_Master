from data import Onduleur
from treatment import recuperer_donnees_onduleur
from GUI import setup_gui

onduleur = Onduleur()
recuperer_donnees_onduleur(onduleur)

setup_gui(onduleur)