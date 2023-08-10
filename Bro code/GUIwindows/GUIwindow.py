# GUI - graphical user interface
from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() # instantiate an instance of a window
window.geometry("800x600")
window.title("Damrok's first GUI program")

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)
window.config(background="#939393")

window.mainloop() # place window on computer screen, listen for events

