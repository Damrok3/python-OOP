from tkinter import *
from tkinter import colorchooser # this is a submodule which is why it doesn't get imported together with the *

window = Tk()

def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    window.config(bg=colorHex) # change background color

window.geometry("800x600")
button = Button(text="click me", command=click)
button.pack()

window.mainloop()