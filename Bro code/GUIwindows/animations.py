from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()


background_photo = PhotoImage(file="wfbackground.png")
background = canvas.create_image(0,0, image=background_photo, anchor = NW)

lissetimage = PhotoImage(file="lisset_sprite.png")
lisset = canvas.create_image(0,0, image=lissetimage, anchor = NW)

lisset_width = lissetimage.width()
lisset_height = lissetimage.height()


while True:
    coordinates = canvas.coords(lisset)
    if (coordinates[0] >= WIDTH - lisset_width or coordinates[0] < 0):
        xVelocity *= -1
    if (coordinates[1] >= HEIGHT - lisset_height or coordinates[1] < 0):
        yVelocity *= -1
    canvas.move(lisset, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()