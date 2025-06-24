from tkinter import * # type: ignore
#from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression_jauge1, recuperer_donnees_pression_jauge2, recuperer_donnees_pression_jauge3, recuperer_donnees_pression_jauge4, recuperer_donnees_pression_jauge5, recuperer_donnees_pression_jauge6
#from treatment import controle_cathode
from data import EtatCathode as etatCathode
from logs import * # type: ignore
from PIL import Image, ImageTk # type: ignore
import time

class Gui:
    def __init__(self, onduleur, pression, cathode, affichage_donnees):
        self.window = Tk()  # Creation of the window (Graphical User Interface)
        self.onduleur = onduleur  # Creation of the onduleur object
        self.pression = pression # Creation of the pression object
        self.cathode = cathode # Creation of the cathode object 
        self.affichage_donnees = affichage_donnees # Creation of the affichage_donnees object
        self.setup_gui()  # Initial configuration of the gui setup

    def setup_gui(self):
        # Get the size of the screen
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Edit of the main features for the window
        self.window.attributes('-fullscreen', YES)
        self.window.configure(bg='#64698A')

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

        self.box1_1.config(highlightcolor='black', highlightthickness=2)

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
        # Onduleur data
        self.text1_box1_1_1 = Label(self.box1_1_1, text="text1_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_box1_1_2 = Label(self.box1_1_2, text="text2_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_box1_1_3 = Label(self.box1_1_3, text="text3_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_box1_1_4 = Label(self.box1_1_4, text="text4_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_box1_1_5 = Label(self.box1_1_5, text="text5_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_box1_1_6 = Label(self.box1_1_6, text="text6_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_box1_1_7 = Label(self.box1_1_7, text="text7_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Pression data
        self.text8_box1_1_8 = Label(self.box1_1_8, text="text8_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text9_box1_1_9 = Label(self.box1_1_9, text="text9_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text10_box1_1_10 = Label(self.box1_1_10, text="text10_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text11_box1_1_11 = Label(self.box1_1_11, text="text11_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text12_box1_1_12 = Label(self.box1_1_12, text="text12_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text13_box1_1_13 = Label(self.box1_1_13, text="text13_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        self.text1_box1_1_1.grid(row=0, column=1, sticky='nsew')
        self.text2_box1_1_2.grid(row=0, column=1, sticky='nsew')
        self.text3_box1_1_3.grid(row=0, column=1, sticky='nsew')
        self.text4_box1_1_4.grid(row=0, column=1, sticky='nsew')
        self.text5_box1_1_5.grid(row=0, column=1, sticky='nsew')
        self.text6_box1_1_6.grid(row=0, column=1, sticky='nsew')
        self.text7_box1_1_7.grid(row=0, column=1, sticky='nsew')
        self.text8_box1_1_8.grid(row=0, column=1, sticky='nsew')
        self.text9_box1_1_9.grid(row=0, column=1, sticky='nsew')
        self.text10_box1_1_10.grid(row=0, column=1, sticky='nsew')
        self.text11_box1_1_11.grid(row=0, column=1, sticky='nsew')
        self.text12_box1_1_12.grid(row=0, column=1, sticky='nsew')
        self.text13_box1_1_13.grid(row=0, column=1, sticky='nsew')

        # Logs
        self.textlog1_box1_1 = Label(self.box1_1, text="LOGS", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Add labels inside box1_2
        self.text_box1_2 = Label(self.box1_2, text="text1_box1_2", bg='#64698A', fg='black', font=('Helvetica', 16, 'bold italic'))
        
        self.text_box1_2.pack(expand=YES)

        # Configuration of a grid inside box2
        self.box2.grid_rowconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=0, weight=1)
        self.box2.grid_columnconfigure(index=1, weight=1)
        self.box2.grid_columnconfigure(index=2, weight=1)
        self.box2.grid_columnconfigure(index=3, weight=1)
        self.box2.grid_columnconfigure(index=4, weight=1)

        # Creation of 5 boxes inside box2
        self.box2_1 = Frame(self.box2, bg="#64698A", bd=0)
        self.box2_2 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_3 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_4 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_5 = Frame(self.box2, bg='#64698A', bd=0)
        self.box2_1.grid(row=0, column=0, sticky='nsew')
        self.box2_2.grid(row=0, column=1, sticky='nsew')
        self.box2_3.grid(row=0, column=2, sticky='nsew')
        self.box2_4.grid(row=0, column=3, sticky='nsew')
        self.box2_5.grid(row=0, column=4, sticky='nsew')

        # Add button inside each box
        self.button_box2_1 = Button(self.box2_1, text="Extinction générale progressive", bg='#3f3f3f', fg='red', font=('Helvetica', 16))
        self.button_box2_2 = Button(self.box2_2, text="Refroidissement cathode", bg='#3f3f3f', fg='orange', font=('Helvetica', 16), command=self.bouton_Refroidissement_Cathode)
        self.button_box2_3 = Button(self.box2_3, text="Afficher les LOGS", bg='#3f3f3f', fg='white', font=('Helvetica', 16), command=self.change_state_button_Affichage_Logs)
        self.button_box2_4 = Button(self.box2_4, text="Chauffe cathode", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 16), command=self.bouton_Chauffe_Cathode)
        self.button_box2_5 = Button(self.box2_5, text="Démarrage progressif", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 16))
        self.button_box2_1.pack(expand=YES)
        self.button_box2_2.pack(expand=YES)
        self.button_box2_3.pack(expand=YES)
        self.button_box2_4.pack(expand=YES)
        self.button_box2_5.pack(expand=YES)

        # Show the arrow cursor in Window
        self.window.config(cursor="arrow")

        # Initialisation of the GUI
        self.update_gui()

        # Callback controle_cathode function
        #self.window.after(5400, self.controle_cathode)

        # Bind the images to rescale them later
        self.window.after(500, self.force_initial_resizing)

    def update_gui(self):
        # Get the data from onduleur and pression
        #self.check_logs_with_data(self.onduleur, self.pression)
        #self.recuperer_donnees(self.onduleur, self.pression)

        # Update the widgets of box1_1 if button_box2_3 is in Affichage_donnees's state
        if self.affichage_donnees == True:
            self.text1_box1_1_1.config(text=f"Tension d'entrée (input_voltage) : {self.onduleur.input_voltage} V")
            self.text2_box1_1_2.config(text=f"Fréquence d'entrée (input_frequency) : {self.onduleur.input_frequency} Hz")
            self.text3_box1_1_3.config(text=f"Tension de la batterie (battery_voltage) : {self.onduleur.battery_voltage} V")
            self.text4_box1_1_4.config(text=f"Temps avant extinction de la batterie (battery_runtime) : {self.onduleur.battery_runtime} s")
            self.text5_box1_1_5.config(text=f"Charge de la batterie (battery_charge) : {self.onduleur.battery_charge} %")
            self.text6_box1_1_6.config(text=f"Charge ups (ups_load) : {self.onduleur.ups_load} %")
            self.text7_box1_1_7.config(text=f"Statut ups (ups_status) : {self.onduleur.ups_status}")
            self.text8_box1_1_8.config(text=f"Pression de la 1ère pompe Turbo (Jauge_1_Turbo) : {self.pression.Jauge_1_Turbo}")
            self.text9_box1_1_9.config(text=f"Pression de la 2nde pompe Turbo (Jauge_2_Turbo) : {self.pression.Jauge_2_Turbo}")
            self.text10_box1_1_10.config(text=f"Pression de la 3ème pompe Turbo (Jauge_3_Turbo) : {self.pression.Jauge_3_Turbo}")
            self.text11_box1_1_11.config(text=f"Pression de la 4ème pompe Turbo (Jauge_4_Turbo) : {self.pression.Jauge_4_Turbo}")
            self.text12_box1_1_12.config(text=f"Pression de la pompe primaire (Jauge_5_Primaire) : {self.pression.Jauge_5_Primaire}")
            self.text13_box1_1_13.config(text=f"Pression de la 6ème pompe (Jauge_6_Vide) : {self.pression.Jauge_6_Vide}")
            
            # Gestion des boutons de chauffe et refroidissement de la cathode
            if ((self.cathode.etat == etatCathode.FROIDE) or (self.cathode.etat == etatCathode.CHAUDE)):
                self.button_box2_2.config(state="normal") 
                self.button_box2_4.config(state="normal")
            elif ((self.cathode.etat == etatCathode.REFROIDISSEMENT) or (self.cathode.etat == etatCathode.CHAUFFE)):
                self.button_box2_2.config(state="disabled")
                self.button_box2_4.config(state="disabled")
        else:
            self.text1_box1_1.config(text="LOGS")

        # Callback of this update function after 1 seconde
        self.window.after(1000, self.update_gui)

    def recuperer_donnees(self, onduleur, pression):
        recuperer_donnees_onduleur(onduleur)
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
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_1.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_1 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_1.config(image=self.tk_resized_image_box1_1_1)
            self.label_image_box1_1_1.image = self.tk_resized_image_box1_1_1
            print(f"[resize_image_box1_1_2] called at time: {time.time()} | size: ({width}, {height})")
            print(f"Frame: {self.box1_1_1.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_2(self, event=None):        
        width = self.box1_1_2.winfo_width()
        height = self.box1_1_2.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_2.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_2 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_2.config(image=self.tk_resized_image_box1_1_2)
            self.label_image_box1_1_2.image = self.tk_resized_image_box1_1_2
            print(f"[resize_image_box1_1_2] called at time: {time.time()} | size: ({width}, {height})")
            print(f"Frame: {self.box1_1_2.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_3(self, event=None):
        width = self.box1_1_3.winfo_width()
        height = self.box1_1_3.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_3.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_3 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_3.config(image=self.tk_resized_image_box1_1_3)
            self.label_image_box1_1_3.image = self.tk_resized_image_box1_1_3
            print(f"Frame: {self.box1_1_3.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_4(self, event=None):
        width = self.box1_1_4.winfo_width()
        height = self.box1_1_4.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_4.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_4 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_4.config(image=self.tk_resized_image_box1_1_4)
            self.label_image_box1_1_4.image = self.tk_resized_image_box1_1_4
            print(f"Frame: {self.box1_1_4.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_5(self, event=None):
        width = self.box1_1_5.winfo_width()
        height = self.box1_1_5.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_5.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_5 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_5.config(image=self.tk_resized_image_box1_1_5)
            self.label_image_box1_1_5.image = self.tk_resized_image_box1_1_5
            print(f"Frame: {self.box1_1_5.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_6(self, event=None):
        width = self.box1_1_6.winfo_width()
        height = self.box1_1_6.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_6.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_6 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_6.config(image=self.tk_resized_image_box1_1_6)
            self.label_image_box1_1_6.image = self.tk_resized_image_box1_1_6
            print(f"Frame: {self.box1_1_6.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_7(self, event=None):
        width = self.box1_1_7.winfo_width()
        height = self.box1_1_7.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_7.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_7 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_7.config(image=self.tk_resized_image_box1_1_7)
            self.label_image_box1_1_7.image = self.tk_resized_image_box1_1_7
            print(f"Frame: {self.box1_1_7.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_8(self, event=None):
        width = self.box1_1_8.winfo_width()
        height = self.box1_1_8.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_8.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_8 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_8.config(image=self.tk_resized_image_box1_1_8)
            self.label_image_box1_1_8.image = self.tk_resized_image_box1_1_8
            print(f"Frame: {self.box1_1_8.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_9(self, event=None):
        width = self.box1_1_9.winfo_width()
        height = self.box1_1_9.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_9.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_9 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_9.config(image=self.tk_resized_image_box1_1_9)
            self.label_image_box1_1_9.image = self.tk_resized_image_box1_1_9
            print(f"Frame: {self.box1_1_9.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_10(self, event=None):
        width = self.box1_1_10.winfo_width()
        height = self.box1_1_10.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_10.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_10 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_10.config(image=self.tk_resized_image_box1_1_10)
            self.label_image_box1_1_10.image = self.tk_resized_image_box1_1_10
            print(f"Frame: {self.box1_1_10.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_11(self, event=None):
        width = self.box1_1_11.winfo_width()
        height = self.box1_1_11.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_11.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_11 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_11.config(image=self.tk_resized_image_box1_1_11)
            self.label_image_box1_1_11.image = self.tk_resized_image_box1_1_11
            print(f"Frame: {self.box1_1_11.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_12(self, event=None):
        width = self.box1_1_12.winfo_width()
        height = self.box1_1_12.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_12.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_12 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_12.config(image=self.tk_resized_image_box1_1_12)
            self.label_image_box1_1_12.image = self.tk_resized_image_box1_1_12
            print(f"Frame: {self.box1_1_12.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

    def resize_image_box1_1_13(self, event=None):
        width = self.box1_1_13.winfo_width()
        height = self.box1_1_13.winfo_height()
        new_width = max(1, int(width * 0.3))
        new_height = max(1, int(height * 0.7))
        if width > 0 and height > 0:                
            resized_image = self.image_pillow_box1_1_13.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            self.tk_resized_image_box1_1_13 = ImageTk.PhotoImage(resized_image)
            self.label_image_box1_1_13.config(image=self.tk_resized_image_box1_1_13)
            self.label_image_box1_1_13.image = self.tk_resized_image_box1_1_13
            print(f"Frame: {self.box1_1_13.winfo_name()} | width_box: {width}, height_box: {height} | new size_image: ({new_width}, {new_height})")

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
        self.resize_image_box1_1_8()
        self.resize_image_box1_1_9()
        self.resize_image_box1_1_10()
        self.resize_image_box1_1_11()
        self.resize_image_box1_1_12()
        self.resize_image_box1_1_13()

    def change_state_button_Affichage_Logs(self):
        if self.affichage_donnees == False :
            #self.update_gui()
            self.button_box2_3.config(text="Afficher les LOGS")
            #self.bg_box1_1.place(x=0, y=0, relwidth=1, relheight=1)
            self.hide_logs_box1_1()
            self.show_data_box1_1()
            #self.resize_images()
            #self.update_gui()
            self.affichage_donnees = True
        else:
            #self.update_gui()
            self.button_box2_3.config(text="Afficher les DONNEES")
            #self.bg_box1_1.place_forget()
            self.hide_data_box1_1()
            self.show_logs_box1_1()
            #self.resize_images()
            #self.update_gui()
            self.affichage_donnees = False

        self.update_gui()

    def hide_data_box1_1(self):
        for label in [
            self.label_image_box1_1_1, self.label_image_box1_1_2,
            self.text1_box1_1_1, self.text2_box1_1_2, self.text3_box1_1,
            self.text4_box1_1, self.text5_box1_1, self.text6_box1_1,
            self.text7_box1_1, self.text8_box1_1, self.text9_box1_1,
            self.text10_box1_1, self.text11_box1_1, self.text12_box1_1,
            self.text13_box1_1
        ]:
            label.pack_forget()

    def show_data_box1_1(self):
        for label in [
            self.text1_box1_1_1, self.text2_box1_1_2, self.text3_box1_1,
            self.text4_box1_1, self.text5_box1_1, self.text6_box1_1,
            self.text7_box1_1, self.text8_box1_1, self.text9_box1_1,
            self.text10_box1_1, self.text11_box1_1, self.text12_box1_1,
            self.text13_box1_1
        ]: 
            label.pack(expand=YES)

    def hide_logs_box1_1(self):
        for label in [
            self.textlog1_box1_1
        ]:
            label.pack_forget()

    def show_logs_box1_1(self):
        for label in [
            self.textlog1_box1_1
        ]: 
            label.pack(expand=YES)

    def check_logs_with_data(self, onduleur, pression):
        self.recuperer_donnees(onduleur, pression)

        # INFO Logs
        if(False): # Si le bouton est pressé : Extinction générale progressive.
            logging.INFO("Lancement du programme : Extinction générale progressive.")
        if(False): # Si le bouton est pressé : Refroidissement cathode.
            logging.INFO("Lancement du programme : Refroidissement cathode.")
        if(False): # Si le bouton est pressé : Chauffe cathode.
            logging.INFO("Lancement du programme : Chauffe cathode.")
        if(False): # Si le bouton est pressé : Démarrage progressif.
            logging.INFO("Lancement du programme : Démarrage progressif.")
        if(False): # Message de chauffe de la cathode terminée.
            logging.INFO("Chauffe de la cathode terminée.")
        if(False): # Message de refroidissement de la cathode terminée.
            logging.INFO("Refroidissement de la cathode terminée.")
        if(False): # Message d'allumage de la manip terminé.
            logging.INFO("Allumage de la manip terminé.")
        if(False): # Envoi du sms pour motif de coupure de courant bien envoyé. 
            logging.INFO("Envoi du sms pour motif de coupure de courant bien envoyé.")
        if(False): # "Logs bien envoyées par mail" (mail toutes les semaines pour l'envoi des logs).
            logging.INFO("Logs bien envoyées par mail.")
        if(self.onduleur.ups_status == "OL CHRG"): # Reprise du courant + mail avec temps pendant lequel il n'y avait plus de courant.
            #logging.INFO(f"Temps de coupure du courant : {#calcul du temps de coupure}")
            logging.INFO("Envoi du mail avec le temps de coupure du courant.")
            log_with_cooldown(logging.INFO, "Reprise de courant : Onduleur sur secteur,", 5)

        # WARNING Logs
        if(self.onduleur.ups_status == "OB"): # Coupure de courant.
            log_with_cooldown(logging.WARNING, "Coupure de courant : Onduleur sur batterie", 5)
        if(False): # L'onduleur va se couper dans X minute(s) (environ 2min30) -> arrêt complet progressif lancé.
            logging.WARNING("L'onduleur va se couper dans X minute(s). Processus d'extinction enclenché")
        if(False): # La jauge de pression 1 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 1 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 1 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 1 a dépassé la valeur seuil basse.")
        if(False): # La jauge de pression 2 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 2 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 2 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 2 a dépassé la valeur seuil basse.")
        if(False): # La jauge de pression 3 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 3 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 3 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 3 a dépassé la valeur seuil basse.")
        if(False): # La jauge de pression 4 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 4 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 4 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 4 a dépassé la valeur seuil basse.")
        if(False): # La jauge de pression 5 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 5 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 5 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 5 a dépassé la valeur seuil basse.")
        if(False): # La jauge de pression 6 a dépassé la valeur seuil haute.
            logging.WARNING("La jauge de pression 6 a dépassé la valeur seuil haute.")
        if(False): # La jauge de pression 6 a dépassé la valeur seuil basse.
            logging.WARNING("La jauge de pression 6 a dépassé la valeur seuil basse.")
        
        # CRITICAL Logs
        if(False): # La jauge de pression 1 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 1 a atteint une valeur critique définie.")
        if(False): # La jauge de pression 2 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 2 a atteint une valeur critique définie.")
        if(False): # La jauge de pression 3 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 3 a atteint une valeur critique définie.")
        if(False): # La jauge de pression 4 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 4 a atteint une valeur critique définie.")
        if(False): # La jauge de pression 5 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 5 a atteint une valeur critique définie.")
        if(False): # La jauge de pression 6 a atteint une valeur critique définie.
            logging.CRITICAL("La jauge de pression 6 a atteint une valeur critique définie.")
        if(False): #Arrêt général pour cause onduleurs vides.
            logging.CRITICAL("Arrêt général pour cause onduleurs vides.")
        if(False): # Batterie onduleur morte.
            logging.CRITICAL("Batterie onduleur morte.")

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

        label_2 = Label(popup, text="Entrer l'intensité de consigne (en A, intensité conseillée : [0;9]Ampères)", font=("Arial", 14))
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
            self.cathode.etat = etatCathode.CHAUFFE
            
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
            self.cathode.etat = etatCathode.REFROIDISSEMENT

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