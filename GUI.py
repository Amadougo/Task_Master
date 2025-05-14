from tkinter import *
from treatment import recuperer_donnees_onduleur

text_box1_1 = None 
text_box1_2 = None

# Creation of the window (Graphical User Interface)
window = Tk()

def setup_gui(onduleur):
    global text_box1_1, text_box1_2
    # Get the size of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Edit of the main features for the window
    window.attributes('-fullscreen', YES)
    window.configure(bg='#64698A')

    # Configuration of the main grid (to place boxes in)
    window.grid_rowconfigure(index=0, weight=9) # 1st row takes 90% of the screen
    window.grid_rowconfigure(index=1, weight=1) # 2nd row takes 10% of the screen
    window.grid_columnconfigure(index=0, weight=1) # 1st and only column takes the whole space

    # Creation of 2 boxes
    box1 = Frame(window, bg='#64698A', bd=0)
    box2 = Frame(window, bg='#64698A', bd=0)
    box1.grid(row=0, column=0, sticky='nsew')
    box2.grid(row=1, column=0, sticky='nsew')

    # Configuration of a grid inside box1
    box1.grid_rowconfigure(index=0, weight=1)
    box1.grid_columnconfigure(index=0, weight=1)
    box1.grid_columnconfigure(index=1, weight=1)

    # Creation of 2 boxes inside box1
    box1_1 = Frame(box1, bg='#64698A', bd=0)
    box1_2 = Frame(box1, bg='#64698A', bd=0)
    box1_1.grid(row=0, column=0, sticky='nsew')
    box1_2.grid(row=0, column=1, sticky='nsew')

    # Add labels inside the boxes
    text_box1_1 = Label(box1_1, text="text_box1_1", bg='#64698A', fg='white', font=('Helvetica', 16, 'bold italic'))
    text_box1_2 = Label(box1_2, text="text_box1_2", bg='#64698A', fg='black', font=('Helvetica', 16, 'bold italic'))
    text_box1_1.pack(expand=YES)
    text_box1_2.pack(expand=YES)

    # Configuration of a grid inside box2
    box2.grid_rowconfigure(index=0, weight=1)
    box2.grid_columnconfigure(index=0, weight=1)
    box2.grid_columnconfigure(index=1, weight=1)
    box2.grid_columnconfigure(index=2, weight=1)
    box2.grid_columnconfigure(index=3, weight=1)
    box2.grid_columnconfigure(index=4, weight=1)

    # Creation of 5 boxes inside box2
    box2_1 = Frame(box2, bg='#64698A', bd=0)
    box2_2 = Frame(box2, bg='#64698A', bd=0)
    box2_3 = Frame(box2, bg='#64698A', bd=0)
    box2_4 = Frame(box2, bg='#64698A', bd=0)
    box2_5 = Frame(box2, bg='#64698A', bd=0)
    box2_1.grid(row=0, column=0, sticky='nsew')
    box2_2.grid(row=0, column=1, sticky='nsew')
    box2_3.grid(row=0, column=2, sticky='nsew')
    box2_4.grid(row=0, column=3, sticky='nsew')
    box2_5.grid(row=0, column=4, sticky='nsew')

    # Add button inside each box
    button_box2_1 = Button(box2_1, text="button_box2_1", bg='#64698A', fg='lightgreen', font=('Helvetica', 16))
    button_box2_2 = Button(box2_2, text="button_box2_2", bg='#64698A', fg='orange', font=('Helvetica', 16))
    button_box2_3 = Button(box2_3, text="button_box2_3", bg='#64698A', fg='orange', font=('Helvetica', 16))
    button_box2_4 = Button(box2_4, text="button_box2_4", bg='#64698A', fg='orange', font=('Helvetica', 16))
    button_box2_5 = Button(box2_5, text="button_box2_5", bg='#64698A', fg='red', font=('Helvetica', 16))
    button_box2_1.pack(expand=YES)
    button_box2_2.pack(expand=YES)
    button_box2_3.pack(expand=YES)
    button_box2_4.pack(expand=YES)
    button_box2_5.pack(expand=YES)
    
    # Initialisation of the GUI
    update_gui(onduleur)

    # Display of the window
    window.mainloop()

# -------- Management of the GUI's update -------- #
def update_gui(onduleur):
    global text_box1_1, text_box1_2
    print("Passer par là !")
    recuperer_donnees_onduleur(onduleur)
    text_box1_1.config(text=f"Tension ={onduleur.input_voltage} V")
    text_box1_2.config(text="Mise à jour_box1_2")
    print("Repasser par là !")
    window.after(1000, update_gui, onduleur)

    """
    class GUI:
        def __init__(self, onduleur):
            self.window = Tk()  # Creation of the window (Graphical User Interface)
            self.onduleur = onduleur  # Creation of the onduleur object
            self.setup_gui()  # Initial configuration of the GUI

        def setup_gui(self):
            self.
            # Get the size of the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Edit of the main features for the window
    window.attributes('-fullscreen', YES)
    window.configure(bg='#64698A')

    # Configuration of the main grid (to place boxes in)
    window.grid_rowconfigure(index=0, weight=9) # 1st row takes 90% of the screen
    window.grid_rowconfigure(index=1, weight=1) # 2nd row takes 10% of the screen
    window.grid_columnconfigure(index=0, weight=1) # 1st and only column takes the whole space

    """