from tkinter import *

def openFile():
    print("file has been opened")

def saveFile():
    print("file has been saved")

def cut():
    print("file has been cut")

def copy():
    print("file has been copied")

def paste():
    print("file has been pasted")

window = Tk()

openImage = PhotoImage(file="folder.png")
saveImage = PhotoImage(file="diskette.png")
exitImage = PhotoImage(file="stop.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Times New Roman", 15))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=openFile, image=openImage, compound=LEFT)
fileMenu.add_command(label="Save", command=saveFile, image=saveImage, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=exitImage, compound=LEFT)

editMenu = Menu(menubar, tearoff=0, font=("Times New Roman", 15))
menubar.add_cascade(label="Edit",  menu=editMenu)

editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()