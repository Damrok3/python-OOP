from tkinter import *

def doSomething(event):
    print("you did a thing")

def doSomethingElse(event):
    print("you did a different thing")

def keyPressed(event):
    #print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Return>", doSomething)
window.bind("<q>", doSomethingElse)
window.bind("<Key>", keyPressed)

label = Label(window, font=("Blambot Pro Lite",100))
label.pack()

window.mainloop()
