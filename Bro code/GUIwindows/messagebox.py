from tkinter import *
from tkinter import messagebox # import messagebox library

def click():
    #messagebox.showinfo(title="This is an info message box", message="You are stinky")
   
    #while(True):
        #messagebox.showwarning(title="WARNING", message="YOUR PC HAS BEEN OVERTAKEN BY SPANISH UNIQISITION. DO NOT RESIST")
    
    #messagebox.showerror(title="ERROR", message="your mom is an error")
    
    # if messagebox.askokcancel(title="ask ok cancel", message="do you want to do the thing?"):
    #     print("you did a thing")
    # else:
    #     print("you cancelled a thing")
    
    # if messagebox.askretrycancel(title="ask retry cancel", message="do you want to retry the thing?"):
    #     print("you retried a thing")
    # else:
    #     print("you cancelled a thing")

    # if messagebox.askyesno(title="ask yes or no", message="do you like cake?"):
    #     print("I like cake too")
    # else:
    #     print("why do you even exist")

    # answer = messagebox.askquestion(title="ask question", message="Do you like spaghetti?")
    # if answer == "yes":
    #     print("I like spaghetti too")
    # else:
    #     print("spaghetti hates you too")

    answer = messagebox.askyesnocancel(title="yes no cancel", message="do you like to code", icon="warning")
    if (answer == True):
        print("god have mercy on you")
    elif(answer == False):
        print("the heck are you even doing here")
    else:
        print("you can't run away from my questions")

window = Tk()

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()