from tkinter import * # type: ignore
from tkinter import scrolledtext
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
#from treatment import controle_cathode
from data import EtatCathode
from data import EtatManip
from logs import * # type: ignore
from PIL import Image, ImageTk # type: ignore
import time

class Gui:
    def __init__(self, onduleur1, onduleur2, pression, cathode, etatManip, affichage_donnees, mode_securite_actif):
        self.window = Tk()  # Creation of the window (Graphical User Interface)
        self.onduleur1 = onduleur1  # Creation of the onduleur1 object
        self.onduleur2 = onduleur2  # Creation of the onduleur2 object
        self.pression = pression # Creation of the pression object
        self.cathode = cathode # Creation of the cathode object 
        self.etatManip = etatManip # Creation of the etatManip object 
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
        self.window.configure(bg='#64698A')
        # Redéfinir le comportement de fermeture
        self.window.protocol("WM_DELETE_WINDOW", self.popUpConfirmationQuitterApplication)

        # Configuration of the main grid (to place boxes in)
        self.window.grid_rowconfigure(index=0, weight=9) # 1st row takes 90% of the screen
        self.window.grid_rowconfigure(index=1, weight=1) # 2nd row takes 10% of the screen
        self.window.grid_columnconfigure(index=0, weight=1) # 1st and only column takes the whole space

        # Creation of 2 boxes
        self.box1 = Frame(self.window, bg='#64698A', bd=0)
        self.box2 = Frame(self.window, bg='#64698A', bd=0)
        self.box1.grid(row=0, column=0, sticky='nsew')
        self.box2.grid(row=1, column=0, sticky='nsew')

        # Configuration of a grid inside box1
        self.box1.grid_rowconfigure(index=0, weight=1)
        self.box1.grid_columnconfigure(index=0, weight=1)
        self.box1.grid_columnconfigure(index=1, weight=1)

        # Creation of 2 boxes inside box1
        self.box1_1 = Frame(self.box1, bg='#64698A', bd=0)
        self.box1_2 = Frame(self.box1, bg='#64698A', bd=0)
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
        self.box1_1_1 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_2 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_3 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_4 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_5 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_6 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_7 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_8 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_9 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_10 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_11 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_12 = Frame(self.box1_1, bg='#64698A', bd=0)
        self.box1_1_13 = Frame(self.box1_1, bg='#64698A', bd=0)

        i = 0
        for label in[
            self.box1_1_1, self.box1_1_2, self.box1_1_3, 
            self.box1_1_4, self.box1_1_5, self.box1_1_6, 
            self.box1_1_7, self.box1_1_8, self.box1_1_9, 
            self.box1_1_10, self.box1_1_11, self.box1_1_12, 
            self.box1_1_13,
        ]:
            label.grid_columnconfigure(0, weight=0) # the image dimensions stay fix
            label.grid_columnconfigure(1, weight=1) # the text dimensions will take space left
            label.grid_rowconfigure(0, weight=1)
            label.grid(row=i, column=0, sticky='nsew')
            i = i + 1

        # images in box1_1_1 to box1_1_13
        self.image_pillow_box1_1_1 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_1 = ImageTk.PhotoImage(self.image_pillow_box1_1_1) # Save for TkInter
        self.label_image_box1_1_1 = Label(self.box1_1_1, image=self.tk_image_box1_1_1, bg="#64698A", bd=0)
        self.label_image_box1_1_1.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_2 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_2 = ImageTk.PhotoImage(self.image_pillow_box1_1_2) # Save for TkInter
        self.label_image_box1_1_2 = Label(self.box1_1_2, image=self.tk_image_box1_1_2, bg="#64698A", bd=0)
        self.label_image_box1_1_2.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_3 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_3 = ImageTk.PhotoImage(self.image_pillow_box1_1_3) # Save for TkInter
        self.label_image_box1_1_3 = Label(self.box1_1_3, image=self.tk_image_box1_1_3, bg="#64698A", bd=0)
        self.label_image_box1_1_3.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_4 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_4 = ImageTk.PhotoImage(self.image_pillow_box1_1_4) # Save for TkInter
        self.label_image_box1_1_4 = Label(self.box1_1_4, image=self.tk_image_box1_1_4, bg="#64698A", bd=0)
        self.label_image_box1_1_4.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_5 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_5 = ImageTk.PhotoImage(self.image_pillow_box1_1_5) # Save for TkInter
        self.label_image_box1_1_5 = Label(self.box1_1_5, image=self.tk_image_box1_1_5, bg="#64698A", bd=0)
        self.label_image_box1_1_5.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_6 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_6 = ImageTk.PhotoImage(self.image_pillow_box1_1_6) # Save for TkInter
        self.label_image_box1_1_6 = Label(self.box1_1_6, image=self.tk_image_box1_1_6, bg="#64698A", bd=0)
        self.label_image_box1_1_6.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_7 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_7 = ImageTk.PhotoImage(self.image_pillow_box1_1_7) # Save for TkInter
        self.label_image_box1_1_7 = Label(self.box1_1_7, image=self.tk_image_box1_1_7, bg="#64698A", bd=0)
        self.label_image_box1_1_7.grid(row=0, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_1 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_2_box1_1_1 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_1) # Save for TkInter
        self.label_image_2_box1_1_1 = Label(self.box1_1_1, image=self.tk_image_2_box1_1_1, bg="#64698A", bd=0)
        self.label_image_2_box1_1_1.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_2 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_2_box1_1_2 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_2) # Save for TkInter
        self.label_image_2_box1_1_2 = Label(self.box1_1_2, image=self.tk_image_2_box1_1_2, bg="#64698A", bd=0)
        self.label_image_2_box1_1_2.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_3 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_2_box1_1_3 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_3) # Save for TkInter
        self.label_image_2_box1_1_3 = Label(self.box1_1_3, image=self.tk_image_2_box1_1_3, bg="#64698A", bd=0)
        self.label_image_2_box1_1_3.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_4 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_2_box1_1_4 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_4) # Save for TkInter
        self.label_image_2_box1_1_4 = Label(self.box1_1_4, image=self.tk_image_2_box1_1_4, bg="#64698A", bd=0)
        self.label_image_2_box1_1_4.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_5 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_2_box1_1_5 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_5) # Save for TkInter
        self.label_image_2_box1_1_5 = Label(self.box1_1_5, image=self.tk_image_2_box1_1_5, bg="#64698A", bd=0)
        self.label_image_2_box1_1_5.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_6 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_2_box1_1_6 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_6) # Save for TkInter
        self.label_image_2_box1_1_6 = Label(self.box1_1_6, image=self.tk_image_2_box1_1_6, bg="#64698A", bd=0)
        self.label_image_2_box1_1_6.grid(row=1, column=0, sticky='nsew')

        self.image_2_pillow_box1_1_7 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_2_box1_1_7 = ImageTk.PhotoImage(self.image_2_pillow_box1_1_7) # Save for TkInter
        self.label_image_2_box1_1_7 = Label(self.box1_1_7, image=self.tk_image_2_box1_1_7, bg="#64698A", bd=0)
        self.label_image_2_box1_1_7.grid(row=1, column=0, sticky='nsew')

        self.image_pillow_box1_1_8 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_8 = ImageTk.PhotoImage(self.image_pillow_box1_1_8) # Save for TkInter
        self.label_image_box1_1_8 = Label(self.box1_1_8, image=self.tk_image_box1_1_8, bg="#64698A", bd=0)
        self.label_image_box1_1_8.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_9 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_9 = ImageTk.PhotoImage(self.image_pillow_box1_1_9) # Save for TkInter
        self.label_image_box1_1_9 = Label(self.box1_1_9, image=self.tk_image_box1_1_9, bg="#64698A", bd=0)
        self.label_image_box1_1_9.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_10 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_10 = ImageTk.PhotoImage(self.image_pillow_box1_1_10) # Save for TkInter
        self.label_image_box1_1_10 = Label(self.box1_1_10, image=self.tk_image_box1_1_10, bg="#64698A", bd=0)
        self.label_image_box1_1_10.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_11 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_11 = ImageTk.PhotoImage(self.image_pillow_box1_1_11) # Save for TkInter
        self.label_image_box1_1_11 = Label(self.box1_1_11, image=self.tk_image_box1_1_11, bg="#64698A", bd=0)
        self.label_image_box1_1_11.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_12 = Image.open('assets/Charge_rouge_4.png')
        self.tk_image_box1_1_12 = ImageTk.PhotoImage(self.image_pillow_box1_1_12) # Save for TkInter
        self.label_image_box1_1_12 = Label(self.box1_1_12, image=self.tk_image_box1_1_12, bg="#64698A", bd=0)
        self.label_image_box1_1_12.grid(row=0, column=0, sticky='nsew')

        self.image_pillow_box1_1_13 = Image.open('assets/Charge_rouge_0.png')
        self.tk_image_box1_1_13 = ImageTk.PhotoImage(self.image_pillow_box1_1_13) # Save for TkInter
        self.label_image_box1_1_13 = Label(self.box1_1_13, image=self.tk_image_box1_1_13, bg="#64698A", bd=0)
        self.label_image_box1_1_13.grid(row=0, column=0, sticky='nsew')

        # Add labels inside box1_1
        # Onduleur1 data
        self.text1_box1_1_1 = Label(self.box1_1_1, text="text1_box1_1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_box1_1_2 = Label(self.box1_1_2, text="text2_box1_1_2", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_box1_1_3 = Label(self.box1_1_3, text="text3_box1_1_3", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_box1_1_4 = Label(self.box1_1_4, text="text4_box1_1_4", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_box1_1_5 = Label(self.box1_1_5, text="text5_box1_1_5", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_box1_1_6 = Label(self.box1_1_6, text="text6_box1_1_6", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_box1_1_7 = Label(self.box1_1_7, text="text7_box1_1_7", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Onduleur2 data
        self.text1_2_box1_1_1 = Label(self.box1_1_1, text="text1_2_box1_1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_2_box1_1_2 = Label(self.box1_1_2, text="text2_2_box1_1_2", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_2_box1_1_3 = Label(self.box1_1_3, text="text3_2_box1_1_3", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_2_box1_1_4 = Label(self.box1_1_4, text="text4_2_box1_1_4", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_2_box1_1_5 = Label(self.box1_1_5, text="text5_2_box1_1_5", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_2_box1_1_6 = Label(self.box1_1_6, text="text6_2_box1_1_6", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_2_box1_1_7 = Label(self.box1_1_7, text="text7_2_box1_1_7", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Pression data
        self.text8_box1_1_8 = Label(self.box1_1_8, text="text8_box1_1_8", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text9_box1_1_9 = Label(self.box1_1_9, text="text9_box1_1_9", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text10_box1_1_10 = Label(self.box1_1_10, text="text10_box1_1_10", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text11_box1_1_11 = Label(self.box1_1_11, text="text11_box1_1_11", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text12_box1_1_12 = Label(self.box1_1_12, text="text12_box1_1_12", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text13_box1_1_13 = Label(self.box1_1_13, text="text13_box1_1_13", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        self.text1_box1_1_1.grid(row=0, column=1, sticky='nsew')
        self.text2_box1_1_2.grid(row=0, column=1, sticky='nsew')
        self.text3_box1_1_3.grid(row=0, column=1, sticky='nsew')
        self.text4_box1_1_4.grid(row=0, column=1, sticky='nsew')
        self.text5_box1_1_5.grid(row=0, column=1, sticky='nsew')
        self.text6_box1_1_6.grid(row=0, column=1, sticky='nsew')
        self.text7_box1_1_7.grid(row=0, column=1, sticky='nsew')
        self.text1_2_box1_1_1.grid(row=1, column=1, sticky='nsew')
        self.text2_2_box1_1_2.grid(row=1, column=1, sticky='nsew')
        self.text3_2_box1_1_3.grid(row=1, column=1, sticky='nsew')
        self.text4_2_box1_1_4.grid(row=1, column=1, sticky='nsew')
        self.text5_2_box1_1_5.grid(row=1, column=1, sticky='nsew')
        self.text6_2_box1_1_6.grid(row=1, column=1, sticky='nsew')
        self.text7_2_box1_1_7.grid(row=1, column=1, sticky='nsew')
        self.text8_box1_1_8.grid(row=0, column=1, sticky='nsew')
        self.text9_box1_1_9.grid(row=0, column=1, sticky='nsew')
        self.text10_box1_1_10.grid(row=0, column=1, sticky='nsew')
        self.text11_box1_1_11.grid(row=0, column=1, sticky='nsew')
        self.text12_box1_1_12.grid(row=0, column=1, sticky='nsew')
        self.text13_box1_1_13.grid(row=0, column=1, sticky='nsew')

        # Logs
        self.textlog1_box1_1 = Label(self.box1_1, text="LOGS", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Add labels inside box1_2
        self.text1_box1_2 = Label(self.box1_2, text="text1_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text2_box1_2 = Label(self.box1_2, text="text2_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text3_box1_2 = Label(self.box1_2, text="text3_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text4_box1_2 = Label(self.box1_2, text="text4_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text5_box1_2 = Label(self.box1_2, text="text5_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
        self.text6_box1_2 = Label(self.box1_2, text="text6_box1_2", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))

        self.text1_box1_2.pack(expand=YES)
        self.text2_box1_2.pack(expand=YES)
        self.text3_box1_2.pack(expand=YES)
        self.text4_box1_2.pack(expand=YES)
        self.text5_box1_2.pack(expand=YES)
        self.text6_box1_2.pack(expand=YES)

        # Configuration of a grid inside box2
        self.box2.grid_rowconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=1, weight=1)
        self.box2.grid_columnconfigure(index=2, weight=1)
        self.box2.grid_columnconfigure(index=3, weight=1)
        self.box2.grid_columnconfigure(index=4, weight=1)
        self.box2.grid_columnconfigure(index=5, weight=1)

        # Creation of 5 boxes inside box2
        self.box2_1 = Frame(self.box2, bg="#64698A", bd=0)
        self.box2_2 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_3 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_4 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_5 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_6 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_1.grid(row=0, column=0, sticky='nsew')
        self.box2_2.grid(row=0, column=1, sticky='nsew')
        self.box2_3.grid(row=0, column=2, sticky='nsew')
        self.box2_4.grid(row=0, column=3, sticky='nsew')
        self.box2_5.grid(row=0, column=4, sticky='nsew')
        self.box2_6.grid(row=0, column=5, sticky='nsew')
        

        # Add button inside each box
        self.button_box2_1 = Button(self.box2_1, text="Sécurité : ACTIVÉE", bg="#309641", fg='white', font=('Helvetica', 15), command=self.bouton_changer_mode_Securite)
        self.mode_securite_actif = True
        self.button_box2_2 = Button(self.box2_2, text="Extinction générale progressive", bg='#3f3f3f', fg='red', font=('Helvetica', 15), command=self.changer_EtatManip_Arret_En_Cours)
        self.button_box2_3 = Button(self.box2_3, text="Refroidissement cathode", bg='#3f3f3f', fg='orange', font=('Helvetica', 15), command=self.bouton_Refroidissement_Cathode)
        self.button_box2_4 = Button(self.box2_4, text="Afficher les LOGS", bg='#3f3f3f', fg='white', font=('Helvetica', 15), command=self.change_state_button_Affichage_Logs)
        self.button_box2_5 = Button(self.box2_5, text="Chauffe cathode", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 15), command=self.bouton_Chauffe_Cathode)
        self.button_box2_6 = Button(self.box2_6, text="Démarrage progressif", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 15), command=self.changer_EtatManip_Demarrage)

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

        # Callback controle_cathode function
        #self.window.after(5400, self.controle_cathode)

        # Bind the images to rescale them later
        self.window.after(500, self.force_initial_resizing)

    def update_gui(self):

        print(f"{time.monotonic()}, passage dans update gui")

        # Callback of the gui update function after 1 seconde
        self.window.after(1000, self.update_gui)

        # Get the data from onduleur1 and pression
        # self.check_logs_with_data(self.onduleur1, self.onduleur2, self.pression)

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
            self.text2_box1_2.config(text=f"t_0 : {self.cathode.t_0}")
            self.text3_box1_2.config(text=f"Valeur de tension de la cathode : {self.cathode.tension}")
            self.text4_box1_2.config(text=f"Valeur de courant de la cathode : {self.cathode.courant}")
            self.text5_box1_2.config(text=f"Courant de consigne : {self.cathode.consigne_courant}")
            self.text6_box1_2.config(text=f"Temps de consigne : {self.cathode.consigne_temps}")

            # Gestion des boutons de chauffe et refroidissement de la cathode
            if ((self.cathode.etat == EtatCathode.FROIDE) or (self.cathode.etat == EtatCathode.CHAUDE)):
                # self.button_box2_3.config(state="normal") 
                # self.button_box2_5.config(state="normal") # Fonctionnement normal cathode enlever les commentaires
                self.button_box2_3.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
                self.button_box2_5.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
            elif ((self.cathode.etat == EtatCathode.REFROIDISSEMENT) or (self.cathode.etat == EtatCathode.CHAUFFE)):
                # self.button_box2_3.config(state="disabled")
                # self.button_box2_5.config(state="disabled") # Fonctionnement normal cathode enlever les commentaires
                self.button_box2_3.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement
                self.button_box2_5.config(state="disabled") # A enlever lorsque la cathode sera commandable correctement            
        else:
            # self.textlog1_box1_1.config(text="LOGS")
            NotImplemented # À enlever

        print(f"{time.monotonic()}, fin du passage dans update gui")

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
        width = self.box1_1_4.winfo_width()
        height = self.box1_1_4.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_4.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_4 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_4.config(image=self.tk_resized_image_box1_1_4)
            self.label_image_box1_1_4.image = self.tk_resized_image_box1_1_4
            
    def resize_image_box1_1_5(self, event=None):
        width = self.box1_1_5.winfo_width()
        height = self.box1_1_5.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_5.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_5 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_5.config(image=self.tk_resized_image_box1_1_5)
            self.label_image_box1_1_5.image = self.tk_resized_image_box1_1_5
            
    def resize_image_box1_1_6(self, event=None):
        width = self.box1_1_6.winfo_width()
        height = self.box1_1_6.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_6.resize(
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
        width = self.box1_1_4.winfo_width()
        height = self.box1_1_4.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_4.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_4 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_4.config(image=self.tk_resized_image_2_box1_1_4)
            self.label_image_2_box1_1_4.image = self.tk_resized_image_2_box1_1_4
            
    def resize_image_2_box1_1_5(self, event=None):
        width = self.box1_1_5.winfo_width()
        height = self.box1_1_5.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_5.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_2_box1_1_5 = ImageTk.PhotoImage(resized_image)
            self.label_image_2_box1_1_5.config(image=self.tk_resized_image_2_box1_1_5)
            self.label_image_2_box1_1_5.image = self.tk_resized_image_2_box1_1_5
            
    def resize_image_2_box1_1_6(self, event=None):
        width = self.box1_1_6.winfo_width()
        height = self.box1_1_6.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.6))
        if width > 0 and height > 0:                
            resized_image = self.image_2_pillow_box1_1_6.resize(
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
        print("Passage dans force_initial_resizing")

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
            self.label_image_box1_1_1, self.label_image_box1_1_2, self.label_image_box1_1_3,
            self.label_image_box1_1_4, self.label_image_box1_1_5, self.label_image_box1_1_6,
            self.label_image_box1_1_7, 
            self.label_image_2_box1_1_1, self.label_image_2_box1_1_2, self.label_image_2_box1_1_3,
            self.label_image_2_box1_1_4, self.label_image_2_box1_1_5, self.label_image_2_box1_1_6,
            self.label_image_2_box1_1_7,
            self.label_image_box1_1_8, self.label_image_box1_1_9,
            self.label_image_box1_1_10, self.label_image_box1_1_11, self.label_image_box1_1_12,
            self.label_image_box1_1_13,
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
        self.label_image_box1_1_1.grid(row=0, column=0, sticky='nsew')
        self.text1_box1_1_1.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_2.grid(row=0, column=0, sticky='nsew')
        self.text2_box1_1_2.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_3.grid(row=0, column=0, sticky='nsew')
        self.text3_box1_1_3.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_4.grid(row=0, column=0, sticky='nsew')
        self.text4_box1_1_4.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_5.grid(row=0, column=0, sticky='nsew')
        self.text5_box1_1_5.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_6.grid(row=0, column=0, sticky='nsew')
        self.text6_box1_1_6.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_7.grid(row=0, column=0, sticky='nsew')
        self.text7_box1_1_7.grid(row=0, column=1, sticky='nsew')

        self.label_image_2_box1_1_1.grid(row=1, column=0, sticky='nsew')
        self.text1_2_box1_1_1.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_2.grid(row=1, column=0, sticky='nsew')
        self.text2_2_box1_1_2.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_3.grid(row=1, column=0, sticky='nsew')
        self.text3_2_box1_1_3.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_4.grid(row=1, column=0, sticky='nsew')
        self.text4_2_box1_1_4.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_5.grid(row=1, column=0, sticky='nsew')
        self.text5_2_box1_1_5.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_6.grid(row=1, column=0, sticky='nsew')
        self.text6_2_box1_1_6.grid(row=1, column=1, sticky='nsew')

        self.label_image_2_box1_1_7.grid(row=1, column=0, sticky='nsew')
        self.text7_2_box1_1_7.grid(row=1, column=1, sticky='nsew')

        self.label_image_box1_1_8.grid(row=0, column=0, sticky='nsew')
        self.text8_box1_1_8.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_9.grid(row=0, column=0, sticky='nsew')
        self.text9_box1_1_9.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_10.grid(row=0, column=0, sticky='nsew')
        self.text10_box1_1_10.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_11.grid(row=0, column=0, sticky='nsew')
        self.text11_box1_1_11.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_12.grid(row=0, column=0, sticky='nsew')
        self.text12_box1_1_12.grid(row=0, column=1, sticky='nsew')

        self.label_image_box1_1_13.grid(row=0, column=0, sticky='nsew')
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

    def check_logs_with_data(self, onduleur1, onduleur2, pression):
        self.recuperer_donnees(onduleur1, onduleur2, pression)

        # INFO Logs
        if(False): # Si le bouton est pressé : Extinction générale progressive.
            log_with_cooldown(logging.INFO, "Lancement du programme : Extinction generale progressive.")
        if(False): # Si le bouton est pressé : Refroidissement cathode.
            log_with_cooldown(logging.INFO, "Lancement du programme : Refroidissement cathode.")
        if(False): # Si le bouton est pressé : Chauffe cathode.
            log_with_cooldown(logging.INFO,"Lancement du programme : Chauffe cathode.")
        if(False): # Si le bouton est pressé : Démarrage progressif.
            log_with_cooldown(logging.INFO, "Lancement du programme : Demarrage progressif.")
        if(False): # Message de chauffe de la cathode terminée.
            log_with_cooldown(logging.INFO, "Chauffe de la cathode terminee.")
        if(False): # Message de refroidissement de la cathode terminée.
            log_with_cooldown(logging.INFO, "Refroidissement de la cathode terminee.")
        if(False): # Message d'allumage de la manip terminé.
            log_with_cooldown(logging.INFO, "Allumage de la manip termine.")
        if(False): # Envoi du sms pour motif de coupure de courant bien envoyé. 
            log_with_cooldown(logging.INFO, "Envoi du sms pour motif de coupure de courant bien envoye.")
        if(False): # "Logs bien envoyées par mail" (mail toutes les semaines pour l'envoi des logs).
            log_with_cooldown(logging.INFO, "Logs bien envoyees par mail.")
        if(self.onduleur1.ups_status == "OL CHRG"): # Reprise du courant + mail avec temps pendant lequel il n'y avait plus de courant.
            # log_with_cooldown(logging.INFO, f"Temps de coupure du courant : {#calcul du temps de coupure}")
            log_with_cooldown(logging.INFO, "Reprise de courant : Onduleur1 sur secteur,", 5)

        # WARNING Logs
        if(self.onduleur1.ups_status == "OB"): # Coupure de courant.
            log_with_cooldown(logging.WARNING, "Coupure de courant : Onduleur1 sur batterie", 5)
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
        if(False): # La jauge de pression 5 a dépassé la valeur seuil haute.
            log_with_cooldown(logging.WARNING, "La jauge de pression 5 a depasse la valeur seuil haute.")
        if(False): # La jauge de pression 5 a dépassé la valeur seuil basse.
            log_with_cooldown(logging.WARNING, "La jauge de pression 5 a depasse la valeur seuil basse.")
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
        if(False): # La jauge de pression 5 a atteint une valeur critique définie.
            log_with_cooldown(logging.CRITICAL, "La jauge de pression 5 a atteint une valeur critique definie.")
        if(False): # La jauge de pression 6 a atteint une valeur critique définie.
            log_with_cooldown(logging.CRITICAL, "La jauge de pression 6 a atteint une valeur critique definie.")
        if(False): #Arrêt général pour cause onduleur1 vide.
            log_with_cooldown(logging.CRITICAL, "Arret general pour cause onduleur1 vide.")
        if(False): # Batterie onduleur1 morte.
            log_with_cooldown(logging.CRITICAL, "Batterie onduleur1 morte.")

    def bouton_Chauffe_Cathode(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation chauffe cathode")
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

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir continuer (chauffage de la cathode) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        label_2 = Label(popup, text="Entrer l'intensité de consigne (en A, intensité conseillée : [0.00;9.00]Ampères)", font=("Arial", 14))
        label_2.pack(pady=20)

        # Zone de saisie de l'intensité (en A)
        entry_intensity = Spinbox(popup, from_=0.00, to=9.00, increment=0.01, format="%.2f", width=10)
        entry_intensity.pack()

        label_3 = Label(popup, text="Entrer le temps de consigne (en min, temps conseillé : [30;60]minutes)", font=("Arial", 14))
        label_3.pack(pady=20)

        # Zone de saisie de l'intensité (en min)
        entry_time = Spinbox(popup, from_=0, to=60, increment=1, width=10)
        entry_time.pack()

        def on_yes():
            self.cathode.consigne_courant = entry_intensity.get() # Récupère l'intensité de consigne (en A)
            self.cathode.consigne_temps = entry_time.get() # Récupère le temps de consigne (en min)
            self.cathode.t_0 = time.monotonic()
            self.cathode.etat = EtatCathode.CHAUFFE
            
            print("Action confirmée.")
            popup.destroy()
            print(f"user_input_intensity = {self.cathode.consigne_courant}")
            print(f"user_input_time = {self.cathode.consigne_temps}")

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()

    def bouton_Refroidissement_Cathode(self):
        popup = Toplevel(self.window)
        popup.title("Confirmation refroidissement cathode")
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

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir continuer (refroidissement de la cathode) ?", font=("Arial", 14))
        label_1.pack(pady=40)

        label_2 = Label(popup, text="Entrer l'intensité de consigne (par pas de 0.01 A, intensité conseillée : [0.00;9.00]Ampères)", font=("Arial", 14))
        label_2.pack(pady=20)

        # Zone de saisie de l'intensité (en A) par pas de 0.01A
        entry_intensity = Spinbox(popup, from_=0.00, to=9.00, increment=0.01, format="%.2f", width=10)
        entry_intensity.pack()

        label_3 = Label(popup, text="Entrer le temps de consigne (en min, temps conseillé : [30;60]minutes)", font=("Arial", 14))
        label_3.pack(pady=20)

        # Zone de saisie de l'intensité (en min)
        entry_time = Spinbox(popup, from_=0, to=60, increment=1, width=10)
        entry_time.pack()

        def on_yes():
            self.cathode.consigne_courant = entry_intensity.get()  # Récupère l'intensité de consigne (en A)
            self.cathode.consigne_temps = entry_time.get() # Récupère le temps de consigne (en min)
            self.cathode.t_0 = time.monotonic()
            self.cathode.etat = EtatCathode.REFROIDISSEMENT

            print("Action confirmée.")
            popup.destroy()
            print(f"user_input_intensity = {self.cathode.consigne_courant}")
            print(f"user_input_time = {self.cathode.consigne_temps}")

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

        label_1 = Label(popup, text="Êtes-vous sûr de vouloir changer de mode de sécurité ?", font=("Arial", 14))
        label_1.pack(pady=10)

        label_2 = Label(popup, text="Attention : si la sécurité est désactivée, alors la manip se mettra en arrêt progressif.", font=("Arial", 14))
        label_2.pack(pady=20)

        def on_yes():
            if(self.mode_securite_actif == True):
                self.button_box2_1.config(text="Sécurité : DÉSACTIVÉE", bg="#FF3F3F")
                self.mode_securite_actif = False
                self.etatManip = EtatManip.OFF
            else:
                self.button_box2_1.config(text="Sécurité : ACTIVÉE", bg="#309641")
                self.mode_securite_actif = True

            print(f"{self.etatManip}")
            print(f"Action confirmée.")
            popup.destroy()

        def on_no():
            print(f"Action annulée.")
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
            self.etatManip = EtatManip.DEMARRAGE
            print(f"Action confirmée. {self.etatManip}")
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
            self.etatManip = EtatManip.ARRET_EN_COURS
            print(f"Action confirmée. {self.etatManip}")
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
            self.window.destroy()  # Ferme l'application et le programme de sécurité OIA

        def on_no():
            print("Action annulée.")
            popup.destroy()

        bouton_oui = Button(popup, text="Oui, je suis sûr de mon choix", command=on_yes)
        bouton_oui.pack(pady=5)

        bouton_non = Button(popup, text="Non, je ne veux pas continuer", command=on_no)
        bouton_non.pack()