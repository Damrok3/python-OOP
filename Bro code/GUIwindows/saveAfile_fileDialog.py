from tkinter import *
from tkinter import filedialog
import os
def saveFile():
    file = filedialog.asksaveasfile(initialdir=f"C:\\Users\\{os.getlogin()}\\Desktop",
                                    defaultextension=".txt",
                                    filetypes=[("Text file",".txt"),
                                               ("HTML file", ".html"),
                                               ("All files", ".*"),
                                               ],
                                    )
    if file is None:
        return      # exception handling in case when we leave the dialogue window without selecting an option after clicking "save"
    filetext = str(text.get(1.0, END)) # get input from the text area
    #filetext = input("enter some text: ") # get input from console
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window, text="save", command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()