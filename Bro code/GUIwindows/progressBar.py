from tkinter import *
from tkinter.ttk import *
import time

def start():
    GB = 50
    donwload = 0
    speed = 1
    while(donwload < GB):
        time.sleep(0.05)
        bar["value"]+=(speed/GB)*100
        donwload+=speed
        percent.set(str(int((donwload/GB)*100))+"%")
        text.set(str(donwload)+"/"+str(GB)+" GB completed")
        window.update_idletasks()

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack()

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()