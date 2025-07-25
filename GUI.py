from tkinter import * # type: ignore
from tkinter import scrolledtext
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
from treatment import controle_cathode
from data import EtatCathode, EtatManip, CoupureCourant
from logs import * # type: ignore
from PIL import Image, ImageTk # type: ignore
import time
import threading
from securite import Securite
import subprocess
from treatment import connexion_cathode
from alert import send_email_with_attachment, wait_for_network
from datetime import datetime
from zoneinfo import ZoneInfo

class Gui:
    def __init__(self, onduleur1, onduleur2, pression, cathode, etatManip, securite, coupureCourant, affichage_donnees, mode_securite_actif):
        self.window = Tk()  # Creation of the window (Graphical User Interface)
        self.onduleur1 = onduleur1  # Creation of the onduleur1 object
        self.onduleur2 = onduleur2  # Creation of the onduleur2 object
        self.pression = pression # Creation of the pression object
        self.cathode = cathode # Creation of the cathode object
        self.etatManip = etatManip # Creation of the etatManip object
        self.securite = securite # Creation of the securite object
        self.coupureCourant = coupureCourant # Creation of the coupureCourant object
        self.affichage_donnees = affichage_donnees # Creation of the affichage_donnees object
        self.mode_securite_actif = mode_securite_actif # Creation of the mode_securite_actif object
        self.setup_gui()  # Initial configuration of the gui setup

    def setup_gui(self):
        # Get the size of the screen
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        
        # Titre de la fenêtre
        self.window.title("Interface graphique du programme de sécurité OIA")

        # Edit of the main features for the window
        # Ajout Plein écran avec 'F11' self.window.bind("<F11>", lambda event: self.window.attributes("-fullscreen", not self.window.attributes("-fullscreen")))
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.configure(bg='#242424')
        # Redéfinir le comportement de fermeture
        self.window.protocol("WM_DELETE_WINDOW", self.popUpConfirmationQuitterApplication)

        # Configuration of the main grid (to place boxes in)
        self.window.grid_rowconfigure(index=0, weight=9) # 1st row takes 90% of the screen
        self.window.grid_rowconfigure(index=1, weight=1) # 2nd row takes 10% of the screen
        self.window.grid_columnconfigure(index=0, weight=1) # 1st and only column takes the whole space

        # Creation of 2 boxes
        self.box1 = Frame(self.window, bg='#242424', bd=0)
        self.box2 = Frame(self.window, bg='#242424', bd=0)
        self.box1.grid(row=0, column=0, sticky='nsew')
        self.box2.grid(row=1, column=0, sticky='nsew')

        # Configuration of a grid inside box1
        self.box1.grid_rowconfigure(index=0, weight=1)
        self.box1.grid_columnconfigure(index=0, weight=1)
        self.box1.grid_columnconfigure(index=1, weight=1)

        # Creation of 2 boxes inside box1
        self.box1_1 = Frame(self.box1, bg='#242424', bd=0)
        self.box1_2 = Frame(self.box1, bg='#242424', bd=0)
        self.box1_1.grid(row=0, column=0, sticky='nsew')
        self.box1_2.grid(row=0, column=1, sticky='nsew')

        self.box1_1.config(highlightcolor='white', highlightthickness=2)
        self.box1_2.config(highlightcolor='white', highlightthickness=2)

        """# Add a background image as box1_1 background
        self.image_pillow_box1_1 = Image.open('image_Jauges_Test.jpg')
        self.background_box1_1 = ImageTk.PhotoImage(self.image_pillow_box1_1)
        self.bg_box1_1 = Label(self.box1_1, image=self.background_box1_1)
        self.bg_box1_1.place(x=0, y=0, relwidth=1, relheight=1)"""

        for i in range(13):
            self.box1_1.grid_columnconfigure(0, weight=1)
            self.box1_1.grid_rowconfigure(i, weight=1) # Every box will have same dimensions

        # Boxes which contain image (left) and text (right)
        self.box1_1_1 = Frame(self.box1_1, bg="#242424", bd=0)
        self.box1_1_2 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_3 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_4 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_5 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_6 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_7 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_8 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_9 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_10 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_11 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_12 = Frame(self.box1_1, bg='#242424', bd=0)
        self.box1_1_13 = Frame(self.box1_1, bg='#242424', bd=0)

        # Chargement des images de charges dans des variables
        self.image_pillow_charge_noire_0 = Image.open('assets/Charge_noire/Charge_noire_0.png')
        self.tk_image_charge_noire_0 = ImageTk.PhotoImage(self.image_pillow_charge_noire_0) # Save for TkInter
        self.image_pillow_charge_noire_1 = Image.open('assets/Charge_noire/Charge_noire_1.png')
        self.tk_image_charge_noire_1 = ImageTk.PhotoImage(self.image_pillow_charge_noire_1) # Save for TkInter
        self.image_pillow_charge_noire_2 = Image.open('assets/Charge_noire/Charge_noire_2.png')
        self.tk_image_charge_noire_2 = ImageTk.PhotoImage(self.image_pillow_charge_noire_2) # Save for TkInter
        self.image_pillow_charge_noire_3 = Image.open('assets/Charge_noire/Charge_noire_3.png')
        self.tk_image_charge_noire_3 = ImageTk.PhotoImage(self.image_pillow_charge_noire_3) # Save for TkInter
        self.image_pillow_charge_noire_4 = Image.open('assets/Charge_noire/Charge_noire_4.png')
        self.tk_image_charge_noire_4 = ImageTk.PhotoImage(self.image_pillow_charge_noire_4) # Save for TkInter

        self.image_pillow_charge_rouge_0 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_charge_rouge_0 = ImageTk.PhotoImage(self.image_pillow_charge_rouge_0) # Save for TkInter
        self.image_pillow_charge_rouge_1 = Image.open('assets/Charge_rouge/Charge_rouge_1.png')
        self.tk_image_charge_rouge_1 = ImageTk.PhotoImage(self.image_pillow_charge_rouge_1) # Save for TkInter
        self.image_pillow_charge_rouge_2 = Image.open('assets/Charge_rouge/Charge_rouge_2.png')
        self.tk_image_charge_rouge_2 = ImageTk.PhotoImage(self.image_pillow_charge_rouge_2) # Save for TkInter
        self.image_pillow_charge_rouge_3 = Image.open('assets/Charge_rouge/Charge_rouge_3.png')
        self.tk_image_charge_rouge_3 = ImageTk.PhotoImage(self.image_pillow_charge_rouge_3) # Save for TkInter
        self.image_pillow_charge_rouge_4 = Image.open('assets/Charge_rouge/Charge_rouge_4.png')
        self.tk_image_charge_rouge_4 = ImageTk.PhotoImage(self.image_pillow_charge_rouge_4) # Save for TkInter

        self.image_pillow_charge_verte_0 = Image.open('assets/Charge_verte/Charge_verte_0.png')
        self.tk_image_charge_verte_0 = ImageTk.PhotoImage(self.image_pillow_charge_verte_0) # Save for TkInter
        self.image_pillow_charge_verte_1 = Image.open('assets/Charge_verte/Charge_verte_1.png')
        self.tk_image_charge_verte_1 = ImageTk.PhotoImage(self.image_pillow_charge_verte_1) # Save for TkInter
        self.image_pillow_charge_verte_2 = Image.open('assets/Charge_verte/Charge_verte_2.png')
        self.tk_image_charge_verte_2 = ImageTk.PhotoImage(self.image_pillow_charge_verte_2) # Save for TkInter
        self.image_pillow_charge_verte_3 = Image.open('assets/Charge_verte/Charge_verte_3.png')
        self.tk_image_charge_verte_3 = ImageTk.PhotoImage(self.image_pillow_charge_verte_3) # Save for TkInter
        self.image_pillow_charge_verte_4 = Image.open('assets/Charge_verte/Charge_verte_4.png')
        self.tk_image_charge_verte_4 = ImageTk.PhotoImage(self.image_pillow_charge_verte_4) # Save for TkInter

        i = 0
        for label in[
            self.box1_1_1, self.box1_1_2, self.box1_1_3, 
            self.box1_1_4, self.box1_1_5, self.box1_1_6, 
            self.box1_1_7, self.box1_1_8, self.box1_1_9, 
            self.box1_1_10, self.box1_1_11, self.box1_1_12, 
            self.box1_1_13,
        ]:
            label.grid_columnconfigure(0, weight=1) # the image dimensions stay fix
            label.grid_columnconfigure(1, weight=1) # the text dimensions will take space left
            label.grid_rowconfigure(0, weight=1)
            label.grid(row=i, column=0, sticky='nsew')
            i = i + 1

        # images in box1_1_1 to box1_1_13
        self.image_pillow_box1_1_1 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_1 = ImageTk.PhotoImage(self.image_pillow_box1_1_1) # Save for TkInter
        self.label_image_box1_1_1 = Label(self.box1_1_1, image=self.tk_image_box1_1_1, bg="#242424", bd=0)
        # self.label_image_box1_1_1.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_2 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_2 = ImageTk.PhotoImage(self.image_pillow_box1_1_2) # Save for TkInter
        self.label_image_box1_1_2 = Label(self.box1_1_2, image=self.tk_image_box1_1_2, bg="#242424", bd=0)
        # self.label_image_box1_1_2.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_3 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_3 = ImageTk.PhotoImage(self.image_pillow_box1_1_3) # Save for TkInter
        self.label_image_box1_1_3 = Label(self.box1_1_3, image=self.tk_image_box1_1_3, bg="#242424", bd=0)
        # self.label_image_box1_1_3.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_4 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_4 = ImageTk.PhotoImage(self.image_pillow_box1_1_4) # Save for TkInter
        self.label_image_box1_1_4 = Label(self.box1_1_4, image=self.tk_image_box1_1_4, bg="#242424", bd=0)
        self.label_image_box1_1_4.grid(row=0, column=1, sticky='e')

        self.image_pillow_box1_1_5 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_5 = ImageTk.PhotoImage(self.image_pillow_box1_1_5) # Save for TkInter
        self.label_image_box1_1_5 = Label(self.box1_1_5, image=self.tk_image_box1_1_5, bg="#242424", bd=0)
        self.label_image_box1_1_5.grid(row=0, column=1, sticky='e')

        self.image_pillow_box1_1_6 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_6 = ImageTk.PhotoImage(self.image_pillow_box1_1_6) # Save for TkInter
        self.label_image_box1_1_6 = Label(self.box1_1_6, image=self.tk_image_box1_1_6, bg="#242424", bd=0)
        self.label_image_box1_1_6.grid(row=0, column=1, sticky='e')

        self.image_pillow_box1_1_7 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_7 = ImageTk.PhotoImage(self.image_pillow_box1_1_7) # Save for TkInter
        self.label_image_box1_1_7 = Label(self.box1_1_7, image=self.tk_image_box1_1_7, bg="#242424", bd=0)
        # self.label_image_box1_1_7.grid(row=0, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_1 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_1 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_1) # Save for TkInter
        self.label_image_2_box1_1_1 = Label(self.box1_1_1, image=self.tk_image_2_box1_1_1, bg="#242424", bd=0)
        # self.label_image_2_box1_1_1.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_2 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_2 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_2) # Save for TkInter
        self.label_image_2_box1_1_2 = Label(self.box1_1_2, image=self.tk_image_2_box1_1_2, bg="#242424", bd=0)
        # self.label_image_2_box1_1_2.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_3 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_3 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_3) # Save for TkInter
        self.label_image_2_box1_1_3 = Label(self.box1_1_3, image=self.tk_image_2_box1_1_3, bg="#242424", bd=0)
        # self.label_image_2_box1_1_3.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_4 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_4 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_4) # Save for TkInter
        self.label_image_2_box1_1_4 = Label(self.box1_1_4, image=self.tk_image_2_box1_1_4, bg="#242424", bd=0)
        self.label_image_2_box1_1_4.grid(row=1, column=1, sticky='e')

        self.image_2_pillow_box1_1_5 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_5 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_5) # Save for TkInter
        self.label_image_2_box1_1_5 = Label(self.box1_1_5, image=self.tk_image_2_box1_1_5, bg="#242424", bd=0)
        self.label_image_2_box1_1_5.grid(row=1, column=1, sticky='e')

        self.image_2_pillow_box1_1_6 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_6 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_6) # Save for TkInter
        self.label_image_2_box1_1_6 = Label(self.box1_1_6, image=self.tk_image_2_box1_1_6, bg="#242424", bd=0)
        self.label_image_2_box1_1_6.grid(row=1, column=1, sticky='e')

        self.image_2_pillow_box1_1_7 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_2_box1_1_7 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_7) # Save for TkInter
        self.label_image_2_box1_1_7 = Label(self.box1_1_7, image=self.tk_image_2_box1_1_7, bg="#242424", bd=0)
        # self.label_image_2_box1_1_7.grid(row=1, column=0, sticky='nsew')

        self.image_pillow_box1_1_8 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_8 = ImageTk.PhotoImage(self.image_pillow_box1_1_8) # Save for TkInter
        self.label_image_box1_1_8 = Label(self.box1_1_8, image=self.tk_image_box1_1_8, bg="#242424", bd=0)
        # self.label_image_box1_1_8.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_9 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_9 = ImageTk.PhotoImage(self.image_pillow_box1_1_9) # Save for TkInter
        self.label_image_box1_1_9 = Label(self.box1_1_9, image=self.tk_image_box1_1_9, bg="#242424", bd=0)
        # self.label_image_box1_1_9.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_10 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_10 = ImageTk.PhotoImage(self.image_pillow_box1_1_10) # Save for TkInter
        self.label_image_box1_1_10 = Label(self.box1_1_10, image=self.tk_image_box1_1_10, bg="#242424", bd=0)
        # self.label_image_box1_1_10.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_11 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_11 = ImageTk.PhotoImage(self.image_pillow_box1_1_11) # Save for TkInter
        self.label_image_box1_1_11 = Label(self.box1_1_11, image=self.tk_image_box1_1_11, bg="#242424", bd=0)
        # self.label_image_box1_1_11.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_12 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_12 = ImageTk.PhotoImage(self.image_pillow_box1_1_12) # Save for TkInter
        self.label_image_box1_1_12 = Label(self.box1_1_12, image=self.tk_image_box1_1_12, bg="#242424", bd=0)
        # self.label_image_box1_1_12.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_13 = Image.open('assets/Charge_rouge/Charge_rouge_0.png')
        self.tk_image_box1_1_13 = ImageTk.PhotoImage(self.image_pillow_box1_1_13) # Save for TkInter
        self.label_image_box1_1_13 = Label(self.box1_1_13, image=self.tk_image_box1_1_13, bg="#242424", bd=0)
        # self.label_image_box1_1_13.grid(row=0, column=0, sticky='nsew')

        # Add labels inside box1_1
        # Onduleur1 data
        self.text1_box1_1_1 = Label(self.box1_1_1, text="text1_box1_1_1", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_box1_1_2 = Label(self.box1_1_2, text="text2_box1_1_2", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_box1_1_3 = Label(self.box1_1_3, text="text3_box1_1_3", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_box1_1_4 = Label(self.box1_1_4, text="text4_box1_1_4", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_box1_1_5 = Label(self.box1_1_5, text="text5_box1_1_5", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_box1_1_6 = Label(self.box1_1_6, text="text6_box1_1_6", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_box1_1_7 = Label(self.box1_1_7, text="text7_box1_1_7", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Onduleur2 data
        self.text1_2_box1_1_1 = Label(self.box1_1_1, text="text1_2_box1_1_1", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_2_box1_1_2 = Label(self.box1_1_2, text="text2_2_box1_1_2", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_2_box1_1_3 = Label(self.box1_1_3, text="text3_2_box1_1_3", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_2_box1_1_4 = Label(self.box1_1_4, text="text4_2_box1_1_4", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_2_box1_1_5 = Label(self.box1_1_5, text="text5_2_box1_1_5", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_2_box1_1_6 = Label(self.box1_1_6, text="text6_2_box1_1_6", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_2_box1_1_7 = Label(self.box1_1_7, text="text7_2_box1_1_7", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Pression data
        self.text8_box1_1_8 = Label(self.box1_1_8, text="text8_box1_1_8", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text9_box1_1_9 = Label(self.box1_1_9, text="text9_box1_1_9", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text10_box1_1_10 = Label(self.box1_1_10, text="text10_box1_1_10", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text11_box1_1_11 = Label(self.box1_1_11, text="text11_box1_1_11", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text12_box1_1_12 = Label(self.box1_1_12, text="text12_box1_1_12", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text13_box1_1_13 = Label(self.box1_1_13, text="text13_box1_1_13", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))

        self.text1_box1_1_1.grid(row=0, column=1, sticky='')
        self.text2_box1_1_2.grid(row=0, column=1, sticky='')
        self.text3_box1_1_3.grid(row=0, column=1, sticky='')
        self.text4_box1_1_4.grid(row=0, column=0)
        self.text5_box1_1_5.grid(row=0, column=0)
        self.text6_box1_1_6.grid(row=0, column=0)
        self.text7_box1_1_7.grid(row=0, column=1, sticky='')
        self.text1_2_box1_1_1.grid(row=1, column=1, sticky='')
        self.text2_2_box1_1_2.grid(row=1, column=1, sticky='')
        self.text3_2_box1_1_3.grid(row=1, column=1, sticky='')
        self.text4_2_box1_1_4.grid(row=1, column=0)
        self.text5_2_box1_1_5.grid(row=1, column=0)
        self.text6_2_box1_1_6.grid(row=1, column=0)
        self.text7_2_box1_1_7.grid(row=1, column=1, sticky='')
        self.text8_box1_1_8.grid(row=0, column=1, sticky='')
        self.text9_box1_1_9.grid(row=0, column=1, sticky='')
        self.text10_box1_1_10.grid(row=0, column=1, sticky='')
        self.text11_box1_1_11.grid(row=0, column=1, sticky='')
        self.text12_box1_1_12.grid(row=0, column=1, sticky='')
        self.text13_box1_1_13.grid(row=0, column=1, sticky='')

        # Logs
        self.textlog1_box1_1 = Label(self.box1_1, text="LOGS", bg='#242424', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Add labels inside box1_2
        self.text1_box1_2 = Label(self.box1_2, text="text1_box1_2", bg='#242424', fg='white', font=('Helvetica', 15, 'bold italic'))
        self.text2_box1_2 = Label(self.box1_2, text="text2_box1_2", bg='#242424', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text3_box1_2 = Label(self.box1_2, text="text3_box1_2", bg='#242424', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text4_box1_2 = Label(self.box1_2, text="text4_box1_2", bg='#242424', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text5_box1_2 = Label(self.box1_2, text="text5_box1_2", bg='#242424', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text6_box1_2 = Label(self.box1_2, text="text6_box1_2", bg='#242424', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text7_box1_2 = Label(self.box1_2, text="text7_box1_2", bg="#45464D", fg='lightgreen', font=('Helvetica', 16, 'bold'))

        self.text1_box1_2.pack(expand=YES)
        self.text2_box1_2.pack(expand=YES)
        self.text3_box1_2.pack(expand=YES)
        self.text4_box1_2.pack(expand=YES)
        self.text5_box1_2.pack(expand=YES)
        self.text6_box1_2.pack(expand=YES)
        self.text7_box1_2.pack(expand=YES)

        # Configuration of a grid inside box2
        self.box2.grid_rowconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=1, weight=1)
        self.box2.grid_columnconfigure(index=2, weight=1)
        self.box2.grid_columnconfigure(index=3, weight=1)
        self.box2.grid_columnconfigure(index=4, weight=1)
        self.box2.grid_columnconfigure(index=5, weight=1)
        self.box2.grid_columnconfigure(index=6, weight=1)

        # Creation of 5 boxes inside box2
        self.box2_1 = Frame(self.box2, bg="#242424", bd=0)
        self.box2_2 = Frame(self.box2, bg='#242424', bd=0)
        self.box2_3 = Frame(self.box2, bg='#242424', bd=0)
        self.box2_4 = Frame(self.box2, bg='#242424', bd=0)
        self.box2_5 = Frame(self.box2, bg='#242424', bd=0)
        self.box2_6 = Frame(self.box2, bg='#242424', bd=0)

        self.box2_1.grid(row=0, column=0, sticky='nsew')
        self.box2_2.grid(row=0, column=1, sticky='nsew')
        self.box2_3.grid(row=0, column=2, sticky='nsew')
        self.box2_4.grid(row=0, column=3, sticky='nsew')
        self.box2_5.grid(row=0, column=4, sticky='nsew')
        self.box2_6.grid(row=0, column=5, sticky='nsew')
        

        # Add button inside each box
        self.button_box2_1 = Button(self.box2_1, text="Sécurité : ACTIVÉE", bg="#309641", fg='white', font=('Helvetica', 14), command=self.bouton_changer_mode_Securite)
        self.mode_securite_actif = True
        self.button_box2_2 = Button(self.box2_2, text="Extinction générale progressive", bg='#3f3f3f', fg='red', font=('Helvetica', 14), command=self.changer_EtatManip_Arret_En_Cours)
        self.button_box2_3 = Button(self.box2_3, text="Changement consignes cathode", bg='#3f3f3f', fg='orange', font=('Helvetica', 14), command=self.bouton_ChangementConsignes_Cathode)
        self.button_box2_4 = Button(self.box2_4, text="Afficher les LOGS", bg='#3f3f3f', fg='white', font=('Helvetica', 14), command=self.change_state_button_Affichage_Logs)
        self.button_box2_5 = Button(self.box2_5, text="Reconnexion série cathode", bg='#3f3f3f', fg='lightblue', font=('Helvetica', 14), command=self.bouton_ReconnexionSerie_Cathode)
        self.button_box2_6 = Button(self.box2_6, text="Démarrage progressif", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 14), command=self.changer_EtatManip_Demarrage)

        self.button_box2_1.pack(expand=YES)
        self.button_box2_2.pack(expand=YES)
        self.button_box2_3.pack(expand=YES)
        self.button_box2_4.pack(expand=YES)
        self.button_box2_5.pack(expand=YES)
        self.button_box2_6.pack(expand=YES)

        # Show the arrow cursor in Window
        self.window.config(cursor="arrow")

        # Initialisation of the GUI
        self.update_gui()

        # Bind the images to rescale them later
        # self.configure_initial_resizing()
        self.window.after(500, self.force_initial_resizing)

        # Thread de mise à jour
        self.running = True
        self.update_thread = threading.Thread(target=self.check_logs_with_data, daemon=True)
        self.update_thread.start()
        
        # 2nd Thread de mise à jour
        self.running2 = True
        update_thread2 = threading.Thread(target=self.securite_gui, daemon=True)
        update_thread2.start()

        # 3ème Thread de mise à jour
        self.running3 = True
        update_thread3 = threading.Thread(target=self.controle_cathode_gui, daemon=True)
        update_thread3.start()

        # 4ème Thread de mise à jour
        self.running4 = True
        update_thread4 = threading.Thread(target=self.coupure_de_courant_gui, daemon=True)
        update_thread4.start()

    def update_gui(self):
        # Callback of the gui update function after 1 seconde
        self.window.after(1000, self.update_gui)

        self.etatManip = self.securite.etat_manip

        # Update the widgets of box1_1 if 4 is in Affichage_donnees's state
        if self.affichage_donnees == True:
            self.text1_box1_1_1.config(text=f"Onduleur1: Tension d'entrée (input_voltage) : {self.onduleur1.input_voltage} V")
            self.text2_box1_1_2.config(text=f"Onduleur1: Fréquence d'entrée (input_frequency) : {self.onduleur1.input_frequency} Hz")
            self.text3_box1_1_3.config(text=f"Onduleur1: Tension de la batterie (battery_voltage) : {self.onduleur1.battery_voltage} V")
            self.text4_box1_1_4.config(text=f"Onduleur1: Temps avant extinction de la batterie (battery_runtime) : {self.onduleur1.battery_runtime} s")
            self.text5_box1_1_5.config(text=f"Onduleur1: Charge de la batterie (battery_charge) : {self.onduleur1.battery_charge} %")
            self.text6_box1_1_6.config(text=f"Onduleur1: Charge ups (ups_load) : {self.onduleur1.ups_load} %")
            self.text7_box1_1_7.config(text=f"Onduleur1: Statut ups (ups_status) : {self.onduleur1.ups_status}")
            self.text1_2_box1_1_1.config(text=f"Onduleur2: Tension d'entrée (input_voltage) : {self.onduleur2.input_voltage} V")
            self.text2_2_box1_1_2.config(text=f"Onduleur2: Fréquence d'entrée (input_frequency) : {self.onduleur2.input_frequency} Hz")
            self.text3_2_box1_1_3.config(text=f"Onduleur2: Tension de la batterie (battery_voltage) : {self.onduleur2.battery_voltage} V")
            self.text4_2_box1_1_4.config(text=f"Onduleur2: Temps avant extinction de la batterie (battery_runtime) : {self.onduleur2.battery_runtime} s")
            self.text5_2_box1_1_5.config(text=f"Onduleur2: Charge de la batterie (battery_charge) : {self.onduleur2.battery_charge} %")
            self.text6_2_box1_1_6.config(text=f"Onduleur2: Charge ups (ups_load) : {self.onduleur2.ups_load} %")
            self.text7_2_box1_1_7.config(text=f"Onduleur2: Statut ups (ups_status) : {self.onduleur2.ups_status}")
            self.text8_box1_1_8.config(text=f"Pression de la 1ère pompe Turbo (Jauge_1_Turbo) : {self.pression.Jauge_1_Turbo}")
            self.text9_box1_1_9.config(text=f"Pression de la 2nde pompe Turbo (Jauge_2_Turbo) : {self.pression.Jauge_2_Turbo}")
            self.text10_box1_1_10.config(text=f"Pression de la 3ème pompe Turbo (Jauge_3_Turbo) : {self.pression.Jauge_3_Turbo}")
            self.text11_box1_1_11.config(text=f"Pression de la 4ème pompe Turbo (Jauge_4_Turbo) : {self.pression.Jauge_4_Turbo}")
            self.text12_box1_1_12.config(text=f"Pression de la pompe primaire (Jauge_5_Primaire) : {self.pression.Jauge_5_Primaire}")
            self.text13_box1_1_13.config(text=f"Pression de la 6ème pompe (Jauge_6_Vide) : {self.pression.Jauge_6_Vide}")
            
            self.text1_box1_2.config(text=f"État de la cathode : {self.cathode.etat}")
            self.text2_box1_2.config(text=f"Lancement cathode : {self.cathode.t_0_print}")
            self.text3_box1_2.config(text=f"Valeur de tension de la cathode : {self.cathode.tension}")
            self.text4_box1_2.config(text=f"Valeur de courant de la cathode : {self.cathode.courant}")
            self.text5_box1_2.config(text=f"Courant de consigne : {self.cathode.consigne_courant}")
            self.text6_box1_2.config(text=f"Temps de consigne : {self.cathode.consigne_temps}")
            self.text7_box1_2.config(text=f"Etat de la manip : {self.securite.etat_manip}")
                
            # Gestion des boutons de chauffe et refroidissement de la cathode
            if ((self.cathode.etat == EtatCathode.FROIDE) or (self.cathode.etat == EtatCathode.CHAUDE)):
                self.button_box2_3.config(state="normal") 
                self.button_box2_5.config(state="normal") # Fonctionnement normal cathode enlever les commentaires
                # self.button_box2_3.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
                # self.button_box2_5.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
            elif ((self.cathode.etat == EtatCathode.REFROIDISSEMENT) or (self.cathode.etat == EtatCathode.CHAUFFE)):
                self.button_box2_3.config(state="disabled")
                self.button_box2_5.config(state="disabled") # Fonctionnement normal cathode enlever les commentaires
                # self.button_box2_3.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
                # self.button_box2_5.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement            

        if(int(self.onduleur1.battery_runtime) < 240 or self.pression.pression_seuil_atteinte == True):
            self.button_box2_6.config(state="disabled")
        else:
            self.button_box2_6.config(state="normal")

        if((self.etatManip == EtatManip.FONCTIONNE) and (self.cathode.etat != EtatCathode.CHAUFFE) and (self.cathode.etat != EtatCathode.REFROIDISSEMENT)):
            self.button_box2_3.config(state="normal")
            self.button_box2_5.config(state="normal")
        else:
            self.button_box2_3.config(state="disabled")
            self.button_box2_5.config(state="disabled")

        if(self.cathode.etat == EtatCathode.DECONNECTEE):
            self.button_box2_3.config(state="disabled")

        if(self.cathode.etat == EtatCathode.DECONNECTEE):
            self.button_box2_5.config(state="normal")
        else:
            self.button_box2_5.config(state="disabled")

        # Refroidissement d'urgence de la cathode lors d'un arrêt en cours.
        if((self.cathode.etat == EtatCathode.CHAUDE) and (self.etatManip == EtatManip.ARRET_EN_COURS)):
            self.cathode.etat = EtatCathode.REFROIDISSEMENT
            self.cathode.t_0 = time.monotonic()
            self.cathode.t_0_print = datetime.now(ZoneInfo("Europe/Paris")).strftime("%H:%M:%S")
            self.cathode.i_depart = float(self.cathode.courant)
            self.cathode.consigne_courant = 0.38
            self.cathode.consigne_temps = 5.0
            log_with_cooldown(logging.WARNING, "Refroidissement d'urgence de la cathode lors d'un arrêt en cours.", 600)

        self.force_initial_resizing()

    def recuperer_donnees(self, onduleur1, onduleur2, pression):
        recuperer_donnees_onduleur(onduleur1)
        recuperer_donnees_onduleur(onduleur2)
        recuperer_donnees_pression_jauge1(pression)
        recuperer_donnees_pression_jauge2(pression)
        recuperer_donnees_pression_jauge3(pression)
        recuperer_donnees_pression_jauge4(pression)
        recuperer_donnees_pression_jauge5(pression)
        recuperer_donnees_pression_jauge6(pression)

    def run(self):
        # Display of the window
        self.window.mainloop()

    def resize_image_box1_1(self, event=None):
        width = self.box1_1.winfo_width()
        height = self.box1_1.winfo_height()
        if width > 0 and height > 0:
            resized_image = self.image_pillow_box1_1.resize((width, height), Image.Resampling.LANCZOS)
            self.background_box1_1_resized = ImageTk.PhotoImage(resized_image)
            self.bg_box1_1.config(image=self.background_box1_1_resized)

    def resize_image_box1_1_1(self, event=None):
        width = self.box1_1_1.winfo_width()
        height = self.box1_1_1.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_1.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_1 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_1.config(image=self.tk_resized_image_box1_1_1)
            self.label_image_box1_1_1.image = self.tk_resized_image_box1_1_1
            
    def resize_image_box1_1_2(self, event=None):        
        width = self.box1_1_2.winfo_width()
        height = self.box1_1_2.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_2.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_2 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_2.config(image=self.tk_resized_image_box1_1_2)
            self.label_image_box1_1_2.image = self.tk_resized_image_box1_1_2
            
    def resize_image_box1_1_3(self, event=None):
        width = self.box1_1_3.winfo_width()
        height = self.box1_1_3.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_3.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_3 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_3.config(image=self.tk_resized_image_box1_1_3)
            self.label_image_box1_1_3.image = self.tk_resized_image_box1_1_3
            
    def resize_image_box1_1_4(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur1.battery_runtime) >= 1800):
                img = self.image_pillow_charge_verte_4
            elif((int(self.onduleur1.battery_runtime) > 600) and (int(self.onduleur1.battery_runtime) <= 1800)):
                img = self.image_pillow_charge_rouge_3
            elif((int(self.onduleur1.battery_runtime) > 240) and (int(self.onduleur1.battery_runtime) <= 600)):
                img = self.image_pillow_charge_rouge_2
            elif((int(self.onduleur1.battery_runtime) > 30) and (int(self.onduleur1.battery_runtime) < 240)):
                img = self.image_pillow_charge_rouge_1
            elif(int(self.onduleur1.battery_runtime) <= 30):
                img = self.image_pillow_charge_rouge_0
            
            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_4 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_4.config(image=self.tk_resized_image_box1_1_4)
            self.label_image_box1_1_4.image = self.tk_resized_image_box1_1_4
            
    def resize_image_box1_1_5(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur1.battery_charge) >= 100):
                img = self.image_pillow_charge_verte_4
            elif((int(self.onduleur1.battery_charge) >= 75) and (int(self.onduleur1.battery_charge) < 100)):
                img = self.image_pillow_charge_noire_4
            elif((int(self.onduleur1.battery_charge) >= 50) and (int(self.onduleur1.battery_charge) < 75)):
                img = self.image_pillow_charge_noire_3
            elif((int(self.onduleur1.battery_charge) >= 25) and (int(self.onduleur1.battery_charge) < 50)):
                img = self.image_pillow_charge_noire_2
            elif((int(self.onduleur1.battery_charge) > 0) and (int(self.onduleur1.battery_charge) < 25)):
                img = self.image_pillow_charge_rouge_1
            elif(int(self.onduleur1.battery_charge) == 0):
                img = self.image_pillow_charge_rouge_0
            
            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_5 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_5.config(image=self.tk_resized_image_box1_1_5)
            self.label_image_box1_1_5.image = self.tk_resized_image_box1_1_5
            
    def resize_image_box1_1_6(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur1.ups_load) >= 100):
                img = self.image_pillow_charge_rouge_4
            elif((int(self.onduleur1.ups_load) >= 75) and (int(self.onduleur1.ups_load) < 100)):
                img = self.image_pillow_charge_noire_4
            elif((int(self.onduleur1.ups_load) >= 50) and (int(self.onduleur1.ups_load) < 75)):
                img = self.image_pillow_charge_noire_3
            elif((int(self.onduleur1.ups_load) >= 25) and (int(self.onduleur1.ups_load) < 50)):
                img = self.image_pillow_charge_noire_2
            elif((int(self.onduleur1.ups_load) > 0) and (int(self.onduleur1.ups_load) < 25)):
                img = self.image_pillow_charge_verte_1
            elif(int(self.onduleur1.ups_load) == 0):
                img = self.image_pillow_charge_verte_0
            
            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_6 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_6.config(image=self.tk_resized_image_box1_1_6)
            self.label_image_box1_1_6.image = self.tk_resized_image_box1_1_6
            
    def resize_image_box1_1_7(self, event=None):
        width = self.box1_1_7.winfo_width()
        height = self.box1_1_7.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_7.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_7 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_7.config(image=self.tk_resized_image_box1_1_7)
            self.label_image_box1_1_7.image = self.tk_resized_image_box1_1_7
            
    def resize_image_2_box1_1_1(self, event=None):
        width = self.box1_1_1.winfo_width()
        height = self.box1_1_1.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_1.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_1 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_1.config(image=self.tk_resized_image_2_box1_1_1)
            self.label_image_2_box1_1_1.image = self.tk_resized_image_2_box1_1_1
            
    def resize_image_2_box1_1_2(self, event=None):        
        width = self.box1_1_2.winfo_width()
        height = self.box1_1_2.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_2.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_2 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_2.config(image=self.tk_resized_image_2_box1_1_2)
            self.label_image_2_box1_1_2.image = self.tk_resized_image_2_box1_1_2
            
    def resize_image_2_box1_1_3(self, event=None):
        width = self.box1_1_3.winfo_width()
        height = self.box1_1_3.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_3.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_3 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_3.config(image=self.tk_resized_image_2_box1_1_3)
            self.label_image_2_box1_1_3.image = self.tk_resized_image_2_box1_1_3
            
    def resize_image_2_box1_1_4(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur2.battery_runtime) >= 1800):
                img = self.image_pillow_charge_verte_4
            elif((int(self.onduleur2.battery_runtime) > 600) and (int(self.onduleur2.battery_runtime) <= 1800)):
                img = self.image_pillow_charge_rouge_3
            elif((int(self.onduleur2.battery_runtime) > 240) and (int(self.onduleur2.battery_runtime) <= 600)):
                img = self.image_pillow_charge_rouge_2
            elif((int(self.onduleur2.battery_runtime) > 30) and (int(self.onduleur2.battery_runtime) < 240)):
                img = self.image_pillow_charge_rouge_1
            elif(int(self.onduleur2.battery_runtime) <= 30):
                img = self.image_pillow_charge_rouge_0

            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_4 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_4.config(image=self.tk_resized_image_2_box1_1_4)
            self.label_image_2_box1_1_4.image = self.tk_resized_image_2_box1_1_4
            
    def resize_image_2_box1_1_5(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur2.battery_charge) >= 100):
                img = self.image_pillow_charge_verte_4
            elif((int(self.onduleur2.battery_charge) >= 75) and (int(self.onduleur2.battery_charge) < 100)):
                img = self.image_pillow_charge_noire_4
            elif((int(self.onduleur2.battery_charge) >= 50) and (int(self.onduleur2.battery_charge) < 75)):
                img = self.image_pillow_charge_noire_3
            elif((int(self.onduleur2.battery_charge) >= 25) and (int(self.onduleur2.battery_charge) < 50)):
                img = self.image_pillow_charge_noire_2
            elif((int(self.onduleur2.battery_charge) > 0) and (int(self.onduleur2.battery_charge) < 25)):
                img = self.image_pillow_charge_rouge_1
            elif(int(self.onduleur2.battery_charge) == 0):
                img = self.image_pillow_charge_rouge_0

            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_5 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_5.config(image=self.tk_resized_image_2_box1_1_5)
            self.label_image_2_box1_1_5.image = self.tk_resized_image_2_box1_1_5
            
    def resize_image_2_box1_1_6(self, event=None):
        width = 500
        height = 80
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            if(int(self.onduleur2.ups_load) >= 100):
                img = self.image_pillow_charge_rouge_4
            elif((int(self.onduleur2.ups_load) >= 75) and (int(self.onduleur2.ups_load) < 100)):
                img = self.image_pillow_charge_noire_4
            elif((int(self.onduleur2.ups_load) >= 50) and (int(self.onduleur2.ups_load) < 75)):
                img = self.image_pillow_charge_noire_3
            elif((int(self.onduleur2.ups_load) >= 25) and (int(self.onduleur2.ups_load) < 50)):
                img = self.image_pillow_charge_noire_2
            elif((int(self.onduleur2.ups_load) > 0) and (int(self.onduleur2.ups_load) < 25)):
                img = self.image_pillow_charge_verte_1
            elif(int(self.onduleur2.ups_load) == 0):
                img = self.image_pillow_charge_verte_0

            resized_image = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_6 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_6.config(image=self.tk_resized_image_2_box1_1_6)
            self.label_image_2_box1_1_6.image = self.tk_resized_image_2_box1_1_6
            
    def resize_image_2_box1_1_7(self, event=None):
        width = self.box1_1_7.winfo_width()
        height = self.box1_1_7.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_7.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_7 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_7.config(image=self.tk_resized_image_2_box1_1_7)
            self.label_image_2_box1_1_7.image = self.tk_resized_image_2_box1_1_7
            
    def resize_image_box1_1_8(self, event=None):
        width = self.box1_1_8.winfo_width()
        height = self.box1_1_8.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_8.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_8 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_8.config(image=self.tk_resized_image_box1_1_8)
            self.label_image_box1_1_8.image = self.tk_resized_image_box1_1_8
            
    def resize_image_box1_1_9(self, event=None):
        width = self.box1_1_9.winfo_width()
        height = self.box1_1_9.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_9.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_9 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_9.config(image=self.tk_resized_image_box1_1_9)
            self.label_image_box1_1_9.image = self.tk_resized_image_box1_1_9
            
    def resize_image_box1_1_10(self, event=None):
        width = self.box1_1_10.winfo_width()
        height = self.box1_1_10.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_10.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_10 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_10.config(image=self.tk_resized_image_box1_1_10)
            self.label_image_box1_1_10.image = self.tk_resized_image_box1_1_10
            
    def resize_image_box1_1_11(self, event=None):
        width = self.box1_1_11.winfo_width()
        height = self.box1_1_11.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_11.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_11 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_11.config(image=self.tk_resized_image_box1_1_11)
            self.label_image_box1_1_11.image = self.tk_resized_image_box1_1_11
            
    def resize_image_box1_1_12(self, event=None):
        width = self.box1_1_12.winfo_width()
        height = self.box1_1_12.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_12.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_12 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_12.config(image=self.tk_resized_image_box1_1_12)
            self.label_image_box1_1_12.image = self.tk_resized_image_box1_1_12
            
    def resize_image_box1_1_13(self, event=None):
        width = self.box1_1_13.winfo_width()
        height = self.box1_1_13.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_13.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_13 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_13.config(image=self.tk_resized_image_box1_1_13)
            self.label_image_box1_1_13.image = self.tk_resized_image_box1_1_13
            
    def configure_initial_resizing(self):
        self.box1_1_1.bind("<Configure>", self.resize_image_box1_1_1)
        self.box1_1_2.bind("<Configure>", self.resize_image_box1_1_2)
        self.box1_1_3.bind("<Configure>", self.resize_image_box1_1_3)
        self.box1_1_4.bind("<Configure>", self.resize_image_box1_1_4)
        self.box1_1_5.bind("<Configure>", self.resize_image_box1_1_5)
        self.box1_1_6.bind("<Configure>", self.resize_image_box1_1_6)
        self.box1_1_7.bind("<Configure>", self.resize_image_box1_1_7)
        self.box1_1_8.bind("<Configure>", self.resize_image_box1_1_8)
        self.box1_1_9.bind("<Configure>", self.resize_image_box1_1_9)
        self.box1_1_10.bind("<Configure>", self.resize_image_box1_1_10)
        self.box1_1_11.bind("<Configure>", self.resize_image_box1_1_11)
        self.box1_1_12.bind("<Configure>", self.resize_image_box1_1_12)
        self.box1_1_13.bind("<Configure>", self.resize_image_box1_1_13)

    def force_initial_resizing(self):
        self.resize_image_box1_1_1()
        self.resize_image_box1_1_2()
        self.resize_image_box1_1_3()
        self.resize_image_box1_1_4()
        self.resize_image_box1_1_5()
        self.resize_image_box1_1_6()
        self.resize_image_box1_1_7()
        self.resize_image_2_box1_1_1()
        self.resize_image_2_box1_1_2()
        self.resize_image_2_box1_1_3()
        self.resize_image_2_box1_1_4()
        self.resize_image_2_box1_1_5()
        self.resize_image_2_box1_1_6()
        self.resize_image_2_box1_1_7()
        self.resize_image_box1_1_8()
        self.resize_image_box1_1_9()
        self.resize_image_box1_1_10()
        self.resize_image_box1_1_11()
        self.resize_image_box1_1_12()
        self.resize_image_box1_1_13()

    def change_state_button_Affichage_Logs(self):
        if self.affichage_donnees == False :
            #self.update_gui()
            self.button_box2_4.config(text="Afficher les LOGS")
            #self.bg_box1_1.place(x=0, y=0, relwidth=1, relheight=1)
            self.hide_logs_box1_1()
            self.show_data_box1_1()
            # self.show_data_box1_2() # Pas nécessaire
            #self.resize_images()
            #self.update_gui()
            self.affichage_donnees = True
        else:
            #self.update_gui()
            self.button_box2_4.config(text="Afficher les DONNEES")
            #self.bg_box1_1.place_forget()
            self.hide_data_box1_1()
            # self.hide_data_box1_2() # Pas nécessaire
            self.show_logs_box1_1()
            #self.resize_images()
            #self.update_gui()
            self.affichage_donnees = False

        # self.update_gui()

    def hide_data_box1_1(self):
        for label in [
            # self.label_image_box1_1_1, self.label_image_box1_1_2, self.label_image_box1_1_3,
            self.label_image_box1_1_4, self.label_image_box1_1_5, self.label_image_box1_1_6,
            # self.label_image_box1_1_7, 
            # self.label_image_2_box1_1_1, self.label_image_2_box1_1_2, self.label_image_2_box1_1_3,
            self.label_image_2_box1_1_4, self.label_image_2_box1_1_5, self.label_image_2_box1_1_6,
            # self.label_image_2_box1_1_7,
            # self.label_image_box1_1_8, self.label_image_box1_1_9,
            # self.label_image_box1_1_10, self.label_image_box1_1_11, self.label_image_box1_1_12,
            # self.label_image_box1_1_13,
            self.text1_box1_1_1, self.text2_box1_1_2, self.text3_box1_1_3,
            self.text4_box1_1_4, self.text5_box1_1_5, self.text6_box1_1_6,
            self.text7_box1_1_7, 
            self.text1_2_box1_1_1, self.text2_2_box1_1_2, self.text3_2_box1_1_3,
            self.text4_2_box1_1_4, self.text5_2_box1_1_5, self.text6_2_box1_1_6,
            self.text7_2_box1_1_7,
            self.text8_box1_1_8, self.text9_box1_1_9,
            self.text10_box1_1_10, self.text11_box1_1_11, self.text12_box1_1_12,
            self.text13_box1_1_13
        ]:
            label.grid_forget()

    def show_data_box1_1(self):
        # self.label_image_box1_1_1.grid(row=0, column=0, sticky='nsew')
        self.text1_box1_1_1.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_2.grid(row=0, column=0, sticky='nsew')
        self.text2_box1_1_2.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_3.grid(row=0, column=0, sticky='nsew')
        self.text3_box1_1_3.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_4.grid(row=0, column=1, sticky='e')
        self.text4_box1_1_4.grid(row=0, column=0)

        self.label_image_box1_1_5.grid(row=0, column=1, sticky='e')
        self.text5_box1_1_5.grid(row=0, column=0)

        self.label_image_box1_1_6.grid(row=0, column=1, sticky='e')
        self.text6_box1_1_6.grid(row=0, column=0)

        # self.label_image_box1_1_7.grid(row=0, column=0, sticky='nsew')
        self.text7_box1_1_7.grid(row=0, column=1, sticky='nsew')

        # self.label_image_2_box1_1_1.grid(row=1, column=0, sticky='nsew')
        self.text1_2_box1_1_1.grid(row=1, column=1, sticky='nsew')

        # self.label_image_2_box1_1_2.grid(row=1, column=0, sticky='nsew')
        self.text2_2_box1_1_2.grid(row=1, column=1, sticky='nsew')

        # self.label_image_2_box1_1_3.grid(row=1, column=0, sticky='nsew')
        self.text3_2_box1_1_3.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_4.grid(row=1, column=1, sticky='e')
        self.text4_2_box1_1_4.grid(row=1, column=0)

        self.label_image_2_box1_1_5.grid(row=1, column=1, sticky='e')
        self.text5_2_box1_1_5.grid(row=1, column=0)

        self.label_image_2_box1_1_6.grid(row=1, column=1, sticky='e')
        self.text6_2_box1_1_6.grid(row=1, column=0)

        # self.label_image_2_box1_1_7.grid(row=1, column=0, sticky='nsew')
        self.text7_2_box1_1_7.grid(row=1, column=1, sticky='nsew')

        # self.label_image_box1_1_8.grid(row=0, column=0, sticky='nsew')
        self.text8_box1_1_8.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_9.grid(row=0, column=0, sticky='nsew')
        self.text9_box1_1_9.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_10.grid(row=0, column=0, sticky='nsew')
        self.text10_box1_1_10.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_11.grid(row=0, column=0, sticky='nsew')
        self.text11_box1_1_11.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_12.grid(row=0, column=0, sticky='nsew')
        self.text12_box1_1_12.grid(row=0, column=1, sticky='nsew')

        # self.label_image_box1_1_13.grid(row=0, column=0, sticky='nsew')
        self.text13_box1_1_13.grid(row=0, column=1, sticky='nsew')

    def hide_data_box1_2(self):
        for label in [
            self.text1_box1_2, self.text2_box1_2, self.text3_box1_2,
            self.text4_box1_2, self.text5_box1_2, self.text6_box1_2
        ]:
            label.pack_forget()

    def show_data_box1_2(self):
        for label in [
            self.text1_box1_2, self.text2_box1_2, self.text3_box1_2,
            self.text4_box1_2, self.text5_box1_2, self.text6_box1_2
        ]: 
            label.pack(expand=YES)

    def hide_logs_box1_1(self):
        if hasattr(self, 'textlog1_box1_1_widget'):
            self.textlog1_box1_1_widget.grid_forget() 

    def show_logs_box1_1(self):
        # Lire le fichier logs.txt
        try:
            with open("fichier_log.log", "r", encoding="utf-8", errors="replace") as file:
                contenu = file.read()
        except FileNotFoundError:
            contenu = "Fichier de logs introuvable."

        # Si le widget n'existe pas encore, on le crée
        if not hasattr(self, 'textlog1_box1_1_widget'):
            self.textlog1_box1_1_widget = scrolledtext.ScrolledText(
                self.box1_1,
                wrap='word',
                bg='#1e1e1e',
                fg='white',
                font=('Consolas', 11),
                borderwidth=0
            )

        # Remettre le widget dans le layout
        self.textlog1_box1_1_widget.grid(row=0, column=0, rowspan=13, columnspan=1, sticky='nsew')

        # Mettre à jour le contenu
        self.textlog1_box1_1_widget.delete('1.0', END)
        self.textlog1_box1_1_widget.insert(INSERT, contenu)

    def check_logs_with_data(self):
        while self.running:
            self.recuperer_donnees(self.onduleur1, self.onduleur2, self.pression)

            # INFO Logs
            if(False): # Si le bouton est pressé : Extinction générale progressive.
                return # log_with_cooldown(logging.INFO, "Lancement du programme : Extinction generale progressive.")
            if(False): # Si le bouton est pressé : Refroidissement cathode.
                return # log_with_cooldown(logging.INFO, "Lancement du programme : Refroidissement cathode.")
            if(False): # Si le bouton est pressé : Chauffe cathode.
                return # log_with_cooldown(logging.INFO,"Lancement du programme : Chauffe cathode.")
            if(False): # Si le bouton est pressé : Démarrage progressif.
                return # log_with_cooldown(logging.INFO, "Lancement du programme : Demarrage progressif.")
            if(False): # Message de chauffe de la cathode terminée.
                return # log_with_cooldown(logging.INFO, "Chauffe de la cathode terminee.")
            if(False): # Message de refroidissement de la cathode terminée.
                return # log_with_cooldown(logging.INFO, "Refroidissement de la cathode terminee.")
            if(False): # Message d'allumage de la manip terminé.
                log_with_cooldown(logging.INFO, "Allumage de la manip termine.")
            if(False): # Envoi du sms pour motif de coupure de courant bien envoyé. 
                log_with_cooldown(logging.INFO, "Envoi du sms pour motif de coupure de courant bien envoye.")
            if(False): # "Logs bien envoyées par mail" (mail toutes les semaines pour l'envoi des logs).
                log_with_cooldown(logging.INFO, "Logs bien envoyees par mail.")
            """if(self.onduleur1.ups_status == "OL CHRG"): # Reprise du courant + mail avec temps pendant lequel il n'y avait plus de courant.
                # log_with_cooldown(logging.INFO, f"Temps de coupure du courant : {#calcul du temps de coupure}")
                return #### log_with_cooldown(logging.INFO, "Reprise de courant : Onduleur1 sur secteur,", 5)"""

            # WARNING Logs
            if(self.onduleur1.ups_status == "OB"): # Coupure de courant.
                log_with_cooldown(logging.WARNING, "Coupure de courant : Onduleur1 sur batterie", 30)
            if(False): # L'onduleur1 va se couper dans X minute(s) (environ 2min30) -> arrêt complet progressif lancé.
                log_with_cooldown(logging.WARNING, "L'onduleur1 va se couper dans X minute(s). Processus d'extinction enclenche")
            if(False): # La jauge de pression 1 a dépassé la valeur seuil haute.
                log_with_cooldown(logging.WARNING, "La jauge de pression 1 a depasse la valeur seuil haute.")
            if(False): # La jauge de pression 1 a dépassé la valeur seuil basse.
                logging.warning("La jauge de pression 1 a depasse la valeur seuil basse.")
            if(False): # La jauge de pression 2 a dépassé la valeur seuil haute.
                log_with_cooldown(logging.WARNING, "La jauge de pression 2 a depasse la valeur seuil haute.")
            if(False): # La jauge de pression 2 a dépassé la valeur seuil basse.
                log_with_cooldown(logging.WARNING, "La jauge de pression 2 a depasse la valeur seuil basse.")
            if(False): # La jauge de pression 3 a dépassé la valeur seuil haute.
                log_with_cooldown(logging.WARNING, "La jauge de pression 3 a depasse la valeur seuil haute.")
            if(False): # La jauge de pression 3 a dépassé la valeur seuil basse.
                log_with_cooldown(logging.WARNING, "La jauge de pression 3 a depasse la valeur seuil basse.")
            if(False): # La jauge de pression 4 a dépassé la valeur seuil haute.
                log_with_cooldown(logging.WARNING, "La jauge de pression 4 a depasse la valeur seuil haute.")
            if(False): # La jauge de pression 4 a dépassé la valeur seuil basse.
                log_with_cooldown(logging.WARNING, "La jauge de pression 4 a depasse la valeur seuil basse.")
            if(False): # La jauge de pression 5 a dépassé la valeur seuil de {PRESSION_SEUIL_PRIMAIRE} mbar.
                log_with_cooldown(logging.WARNING, "La jauge de pression 5 a depasse la valeur seuil de {PRESSION_SEUIL_PRIMAIRE} mbar.")
            if(False): # La jauge de pression 6 a dépassé la valeur seuil haute.
                log_with_cooldown(logging.WARNING, "La jauge de pression 6 a depasse la valeur seuil haute.")
            if(False): # La jauge de pression 6 a dépassé la valeur seuil basse.
                log_with_cooldown(logging.WARNING, "La jauge de pression 6 a depasse la valeur seuil basse.")
            
            # CRITICAL Logs
            if(False): # La jauge de pression 1 a atteint une valeur critique définie.
                log_with_cooldown(logging.CRITICAL, "La jauge de pression 1 a atteint une valeur critique definie.")
            if(False): # La jauge de pression 2 a atteint une valeur critique définie.
                log_with_cooldown(logging.CRITICAL, "La jauge de pression 2 a atteint une valeur critique definie.")
            if(False): # La jauge de pression 3 a atteint une valeur critique définie.
                log_with_cooldown(logging.CRITICAL, "La jauge de pression 3 a atteint une valeur critique definie.")
            if(False): # La jauge de pression 4 a atteint une valeur critique définie.
                log_with_cooldown(logging.CRITICAL, "La jauge de pression 4 a atteint une valeur critique definie.")
            if(False): # La jauge de pression 5 a atteint une valeur critique de {PRESSION_SEUIL_PRIMAIRE} mbar.
                return # log_with_cooldown(logging.CRITICAL, f"La jauge de pression 5 a depasse la valeur seuil de {PRESSION_SEUIL_PRIMAIRE} mbar.")
            if(False): # La jauge de pression 6 a atteint une valeur critique définie.
                log_with_cooldown(logging.CRITICAL, "La jauge de pression 6 a atteint une valeur critique definie.")
            if(False): #Arrêt général pour cause onduleur1 presque vide (4 minutes restantes avant batteries vides).
                return # log_with_cooldown(logging.CRITICAL, "Arret general pour cause onduleur1 presque vide (4 minutes restantes avant batteries vides).")
            if(False): # Batterie onduleur1 morte.
                log_with_cooldown(logging.CRITICAL, "Batterie onduleur1 morte.")

            time.sleep(1) # Fréquence de mise à jour : 1 seconde

    def bouton_ReconnexionSerie_Cathode(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation reconnexion série cathode")
        popup.geometry("800x200")
        popup.transient(self.window) 
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 800
        window_height = 200

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir continuer (reconnexion série de la cathode) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        def on_yes():
            self.cathode.etat = EtatCathode.FROIDE
            connexion_cathode()
            log_with_cooldown(logging.INFO,"Reconnexion série de la cathode...")
            print("Action confirmée.")
            popup.destroy()

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def bouton_ChangementConsignes_Cathode(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation changement consignes cathode")
        popup.geometry("800x400")
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 800
        window_height = 400

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir continuer (changement de consignes de la cathode) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        label_2 = Label(popup, text="Entrer l'intensité de consigne (par pas de 0.01 A, intensité conseillée : [0.00;9.00]Ampères)", font=("Arial", 14))
        label_2.pack(pady=20)

        # Zone de saisie de l'intensité (en A) par pas de 0.01A
        entry_intensity = Spinbox(popup, from_=0.00, to=9.00, increment=0.01, format="%.2f", width=10)
        entry_intensity.pack()

        label_3 = Label(popup, text="Entrer le temps de consigne (en min, temps conseillé : [30;60]minutes)", font=("Arial", 14))
        label_3.pack(pady=20)

        # Zone de saisie de l'intensité (en min)
        entry_time = Spinbox(popup, from_=1, to=60, increment=1, width=10)
        entry_time.pack()

        def on_yes():
            self.cathode.consigne_courant = entry_intensity.get()  # Récupère l'intensité de consigne (en A)
            self.cathode.consigne_temps = entry_time.get() # Récupère le temps de consigne (en min)
            if(float(self.cathode.consigne_courant) >= float(self.cathode.courant)):
                self.cathode.etat = EtatCathode.CHAUFFE
            else:
                self.cathode.etat = EtatCathode.REFROIDISSEMENT
            self.cathode.t_0 = time.monotonic()
            self.cathode.t_0_print = datetime.now(ZoneInfo("Europe/Paris")).strftime("%H:%M:%S")
            self.cathode.i_depart = float(self.cathode.courant)
            log_with_cooldown(logging.INFO, "Lancement du programme : Changement de la consigne de la cathode.")
            print("Action confirmée.")
            popup.destroy()

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def bouton_changer_mode_Securite(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation du changement de mode sécurité")
        popup.geometry("800x220")
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 800
        window_height = 220

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir changer de mode de sécurité ?", font=("Arial", 14))
        label_1.pack(pady=10)

        label_2 = Label(popup, text="Attention : si la sécurité est désactivée,", font=("Arial", 14))
        label_2.pack(pady=20) 

        label_3 = Label(popup, text="alors la vérification des pressions seuils et de la cathode n'est plus faite.", font=("Arial", 14))
        label_3.pack(pady=0) 

        def on_yes():
            if(self.mode_securite_actif == True):
                self.button_box2_1.config(text="Sécurité : DÉSACTIVÉE", bg="#FF3F3F")
                self.mode_securite_actif = False
                self.securite.securite_pression_actif = self.mode_securite_actif
                log_with_cooldown(logging.WARNING, "La sécurité a été désactivé")
            else:
                self.button_box2_1.config(text="Sécurité : ACTIVÉE", bg="#309641")
                self.mode_securite_actif = True
                self.securite.securite_pression_actif = self.mode_securite_actif
                log_with_cooldown(logging.INFO, "La sécurité a été activé")

            print(f"Action confirmée.")
            popup.destroy()

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def changer_EtatManip_Demarrage(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation démarrage progressif de la Manip")
        popup.geometry("1000x200")
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 1000
        window_height = 200

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir démarrer la Manip (Attention : Veuillez vous assurer que les pompes primaires sont actives) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        def on_yes():
            if(int(self.onduleur1.battery_runtime) > 240):
                self.securite.etat_manip = EtatManip.DEMARRAGE
                log_with_cooldown(logging.INFO, "Lancement du programme : Demarrage progressif.")
                popup.destroy()

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def changer_EtatManip_Arret_En_Cours(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation extinction progressive de la Manip")
        popup.geometry("1000x200")
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 1000
        window_height = 200

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir éteindre la Manip (Attention : Veuillez éteindre les pompes primaires par la suite) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        def on_yes():
            self.securite.etat_manip = EtatManip.ARRET_EN_COURS
            log_with_cooldown(logging.INFO, "Lancement du programme : Extinction generale progressive.")
            popup.destroy()

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def popUpConfirmationQuitterApplication(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation de l'arrêt du programme de sécurité OIA")
        popup.geometry("600x200")
        popup.transient(self.window)
        popup.grab_set()
        popup.focus_force()

        # ----- Centrage de la pop up dans l'écran -----
        self.window.update_idletasks()  # Assure les dimensions correctes
        window_width = 600
        window_height = 200

        # Récupère la position de la fenêtre principale
        x = self.window.winfo_x()
        y = self.window.winfo_y()
        w = self.window.winfo_width()
        h = self.window.winfo_height()

        # Calcule les coordonnées pour centrer la popup par rapport à la fenêtre principale
        x_center = x + (w - window_width) // 2
        y_center = y + (h - window_height) // 2

        popup.geometry(f"{window_width}x{window_height}+{x_center}+{y_center}")
        # ---------------------

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir quitter le programme de  sécurité OIA ?", font=("Arial", 14))
        label_1.pack(pady=40)

        def on_yes():
            print("Action confirmée.")
            popup.destroy()
            self.running = False
            self.running2 = False
            self.running3 = False
            self.running4 = False
            time.sleep(2)
            log_with_cooldown(logging.INFO, "Fermeture du programme...")
            self.window.destroy()  # Ferme l'application et le programme de sécurité OIA

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def securite_gui(self):
        time.sleep(10)
        while self.running2:
            self.securite.securite()

            time.sleep(1)

    def controle_cathode_gui(self):
        while self.running3:
            if self.cathode.etat != EtatCathode.DECONNECTEE:
                try:
                    controle_cathode(self.cathode)
                except Exception as e:
                    print(f"Cathode déconnectée : {e}")
                    self.cathode.etat = EtatCathode.DECONNECTEE
            time.sleep(1)

    def coupure_de_courant_gui(self):
        time.sleep(2)
        while self.running4:
            var = self.onduleur1.ups_status
            var = var[:2]
            indicateur = False
            self.coupureCourant.heure_coupure = datetime.now(ZoneInfo("Europe/Paris"))
            
            while(var != "OL"):
                self.coupureCourant.alimentation_secteur = False
                indicateur = True
                log_with_cooldown(logging.CRITICAL, "Coupure de courant détectée ou onduleur1 déconnecté", 60)
                time.sleep(1)

                var = self.onduleur1.ups_status
                var = var[:2]
            else:
                if indicateur:
                    # Calcul du temps de coupure de courant
                    self.coupureCourant.heure_reprise = datetime.now(ZoneInfo("Europe/Paris")).strftime("%Y-%m-%d %H:%M:%S")

                    # On remet le courant en True
                    self.coupureCourant.alimentation_secteur = True
                    log_with_cooldown(logging.INFO, "Reprise de courant : Onduleur1 sur secteur", 1)

                    # Envoi du mail avec le temps de coupure de courant
                    if wait_for_network():
                        send_email_with_attachment(
                            "Alerte : Coupure de courant détectée",
                            f"Une coupure de courant a été détectée à {self.coupureCourant.heure_coupure}. L'alimentation et le réseau sont maintenant rétablis à {self.coupureCourant.heure_reprise}.",
                            "fichier_log.log"
                        )

                    """# Lancement driver onduleur en cas de fin de coupure de courant
                    subprocess.run(["sudo", "upsdrvctl", "start"])"""
            
            time.sleep(1)