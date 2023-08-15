from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)     # widget that manages a collection of windows and displays

tab1 = Frame(notebook)              # new frame for tab1
tab2 = Frame(notebook)              # new frame for tab2

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")          # expand to fill any space not otherwise used
                                                 # fill = fill space on x and y axis

Label(tab1, text="hello, this is tab nr 1", width=50, height=25).pack()
Label(tab2, text="hello, this is tab nr 2", width=50, height=25).pack()


window.mainloop()