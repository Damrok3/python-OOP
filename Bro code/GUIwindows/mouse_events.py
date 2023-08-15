from tkinter import *

def doSomething(event):
    print("mouse coordinates: " + str(event.x) + "," + str(event.y))

window = Tk()

window.bind("<Button-1>",doSomething) # left click
window.bind("<Button-2>",doSomething) # scroll click
window.bind("<Button-3>",doSomething) # right click
window.bind("<ButtonRelease>",doSomething)
window.bind("<Enter>",doSomething) # enter the window
window.bind("<Leave>",doSomething) # leave the window
window.bind("<Motion>",doSomething) # where the mouse moved

window.mainloop()