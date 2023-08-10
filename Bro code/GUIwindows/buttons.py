# button = you click it, then it does stuff

from tkinter import *

window = Tk()

count = 0

def click():
    global count
    count += 1
    print("you clicked the button ", count, " times")

photo = PhotoImage(file="button.png")


button = Button(window,
                text="click me",
                font=("Blambot Pro Lite", 40),
                command=click, # can't add parentheses
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black", # makes the button not to flash when we click it
                state=ACTIVE, 
                image=photo,
                compound="top")   
button.pack()

window.mainloop()
