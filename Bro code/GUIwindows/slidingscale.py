from tkinter import *

def submit():
    print("the temperature is: " + str(scale.get())+" degrees C")

window = Tk()

flameimg = PhotoImage(file="flame.png")
flameLabel = Label(image=flameimg)
flameLabel.pack()

scale = Scale(window,
              from_= 100,
              to = 0,
              length=600,
              orient=VERTICAL, # orientation of scale
              font=("Blambot Pro Lite", 20),
              tickinterval=10, # adds numeric indicators for value
              showvalue=1,
              resolution=5, # increment of slider
              troughcolor="#69eaff",
              fg="#ff1c00",
              bg="black")


scale.set((scale["from"] - scale["to"]) / 2 + scale["to"])
scale.pack()

snowimg = PhotoImage(file="snow.png")
snowLabel = Label(image=snowimg)
snowLabel.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()

