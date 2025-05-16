from tkinter import * # type: ignore
from treatment import recuperer_donnees_onduleur, recuperer_donnees_pression
from PIL import Image, ImageTk # type: ignore

class Gui:
    def __init__(self, onduleur, pression):
        self.window = Tk()  # Creation of the window (Graphical User Interface)
        self.onduleur = onduleur  # Creation of the onduleur object
        self.pression = pression # Creation of the pression object
        self.setup_gui()  # Initial configuration of the GUI

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

        # Add a background image as box1_1 background
        self.image_pillow_box1_1 = Image.open('image_Jauges_Test.jpg')
        self.background_box1_1 = ImageTk.PhotoImage(self.image_pillow_box1_1)
        self.bg_box1_1 = Label(self.box1_1, image=self.background_box1_1)
        self.bg_box1_1.place(x=0, y=0, relwidth=1, relheight=1)

        # Add labels inside box1_1
        # Onduleur data
        self.text1_box1_1 = Label(self.box1_1, text="text1_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text2_box1_1 = Label(self.box1_1, text="text2_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text3_box1_1 = Label(self.box1_1, text="text3_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text4_box1_1 = Label(self.box1_1, text="text4_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text5_box1_1 = Label(self.box1_1, text="text5_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text6_box1_1 = Label(self.box1_1, text="text6_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text7_box1_1 = Label(self.box1_1, text="text7_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        # Pression data
        self.text8_box1_1 = Label(self.box1_1, text="text8_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text9_box1_1 = Label(self.box1_1, text="text9_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text10_box1_1 = Label(self.box1_1, text="text10_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text11_box1_1 = Label(self.box1_1, text="text11_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))
        self.text12_box1_1 = Label(self.box1_1, text="text12_box1_1", bg='#64698A', fg='white', font=('Helvetica', 12, 'bold italic'))

        self.text1_box1_1.pack(expand=YES)
        self.text2_box1_1.pack(expand=YES)
        self.text3_box1_1.pack(expand=YES)
        self.text4_box1_1.pack(expand=YES)
        self.text5_box1_1.pack(expand=YES)
        self.text6_box1_1.pack(expand=YES)
        self.text7_box1_1.pack(expand=YES)
        self.text8_box1_1.pack(expand=YES)
        self.text9_box1_1.pack(expand=YES)
        self.text10_box1_1.pack(expand=YES)
        self.text11_box1_1.pack(expand=YES)
        self.text12_box1_1.pack(expand=YES)

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
        self.box2_1 = Frame(self.box2, bg='#64698A', bd=0)
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
        self.button_box2_2 = Button(self.box2_2, text="button_box2_2 ???", bg='#3f3f3f', fg='orange', font=('Helvetica', 16))
        self.button_box2_3 = Button(self.box2_3, text="Refroidissement cathode", bg='#3f3f3f', fg='orange', font=('Helvetica', 16))
        self.button_box2_4 = Button(self.box2_4, text="Chauffe cathode", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 16))
        self.button_box2_5 = Button(self.box2_5, text="Démarrage progressif", bg='#3f3f3f', fg='lightgreen', font=('Helvetica', 16))
        self.button_box2_1.pack(expand=YES)
        self.button_box2_2.pack(expand=YES)
        self.button_box2_3.pack(expand=YES)
        self.button_box2_4.pack(expand=YES)
        self.button_box2_5.pack(expand=YES)

        # Initialisation of the GUI
        self.update_gui()

        # Bind the images to rescale them later
        self.box1_1.bind("<Configure>", self.resize_images)
        
    def update_gui(self):
        # Get the data from onduleur
        recuperer_donnees_onduleur(self.onduleur)
        recuperer_donnees_pression(self.pression)
        
        # Update the widgets of box1_1
        self.text1_box1_1.config(text=f"Tension d'entrée (input_voltage) : {self.onduleur.input_voltage} V")
        self.text2_box1_1.config(text=f"Fréquence d'entrée (input_frequency) : {self.onduleur.input_frequency} Hz")
        self.text3_box1_1.config(text=f"Tension de la batterie (battery_voltage) : {self.onduleur.battery_voltage} V")
        self.text4_box1_1.config(text=f"Temps avant extinction de la batterie (battery_runtime) : {self.onduleur.battery_runtime} s")
        self.text5_box1_1.config(text=f"Charge de la batterie (battery_charge) : {self.onduleur.battery_charge} %")
        self.text6_box1_1.config(text=f"Charge ups (ups_load) : {self.onduleur.ups_load} %")
        self.text7_box1_1.config(text=f"Statut ups (ups_status) : {self.onduleur.ups_status}")
        self.text8_box1_1.config(text=f"Pression de la 1ère pompe Turbo (Jauge_1_Turbo) : {self.pression.Jauge_1_Turbo} Torr")
        self.text9_box1_1.config(text=f"Pression de la 2nde pompe Turbo (Jauge_2_Turbo) : {self.pression.Jauge_2_Turbo} Torr")
        self.text10_box1_1.config(text=f"Pression de la 3ème pompe Turbo (Jauge_3_Turbo) : {self.pression.Jauge_3_Turbo} Torr")
        self.text11_box1_1.config(text=f"Pression de la 4ème pompe Turbo (Jauge_4_Turbo) : {self.pression.Jauge_4_Turbo} Torr")
        self.text12_box1_1.config(text=f"Pression de la pompe primaire (Jauge_5_Primaire) : {self.pression.Jauge_5_Primaire} Torr")
             
        # Callback of this update function after 1 seconde
        self.window.after(1000, self.update_gui)

    def run(self):
        # Display of the window
        self.window.mainloop()

    def resize_images(self, event=None):
        width = self.box1_1.winfo_width()
        height = self.box1_1.winfo_height()
        if width > 0 and height > 0:
            resized_image = self.image_pillow_box1_1.resize((width, height), Image.Resampling.LANCZOS)
            self.background_box1_1_resized = ImageTk.PhotoImage(resized_image)
            self.bg_box1_1.config(image=self.background_box1_1_resized)