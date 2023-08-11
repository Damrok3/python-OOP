from tkinter import *

def display():
    if(x.get()):
        print("you agree")
    else:
        print("you don't agree")

window = Tk()

x = BooleanVar()

python_icon = PhotoImage(file="pythonlogo.png")

check_button = Checkbutton(window,
                           text = "I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Blambot Pro Lite", 20),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00ff00",
                           activebackground="black",
                           padx=25,
                           pady=10,
                           image=python_icon,
                           compound=LEFT)
check_button.pack()

window.mainloop()