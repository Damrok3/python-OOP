# listbox = A listing of selectable text items within it's own container

from tkinter import *

window = Tk()

def submit():
    print("you have ordered: ")
    #print(listbox.get(listbox.curselection())) # was used when there was only one submit option
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())

def delete():
    #listbox.delete(listbox.curselection()) # was used when there was only one submit option
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Blambot Pro Lite", 35),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()
addButton = Button(window, text="add", command=add)
addButton.pack()
deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()
window.mainloop()

