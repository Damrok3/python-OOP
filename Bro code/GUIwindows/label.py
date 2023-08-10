from tkinter import *

#label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file="icon.png")

label = Label(window,
              text="bro do you even code",
              font=("Blambot Pro Lite", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief="raised",
              bd=10,
              padx=20,
              pady=20,
              image = photo,
              compound="top")
label.pack()
#label.place(x = 100, y = 100)

window.mainloop()