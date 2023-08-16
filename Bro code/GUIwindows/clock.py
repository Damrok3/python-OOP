from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)          # Recursion means that the current instance of a function is placed 
                                        # on hold and a new instance is created and run. after works differently, 
                                        # and is not recursion.
                                        # You can think of the mainloop as an infinite loop that maintains a
                                        # todo list. The list has functions and the time that they ought to be run.

window = Tk()

time_label = Label(window, font=("Blambot Pro Lite", 50), fg="#00ff00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 25))
date_label.pack()

update()

window.mainloop()