from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
                print(indexes)
                for i, j in indexes:
                    buttons[i][j].config(bg="green")
            elif check_winner() == "Tie":
                label.config(text="Tie!")
        else:
            buttons[row][column]["text"] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
                print(indexes)
                for i, j in indexes:
                    buttons[i][j].config(bg="green")
            elif check_winner() == "Tie":
                label.config(text="Tie!")

indexes = []

def check_winner():
    matches = 0
    length = len(buttons) - 1

    #making sure that the function won't fill up the indexes more than once when it's executed couple of times
    if len(indexes) == len(buttons):
        indexes.clear()

    # horizontal check
    for row in range(length):
        for column in range(length):
            if buttons[row][column]["text"] == buttons[row][column + 1]["text"] != "":
                matches+=1
                indexes.append((row, column))
        if matches == length:
            indexes.append((row, column + 1))
            return True
        else:
            matches = 0
            indexes.clear()

    # vertical check
    for column in range(length):
        for row in range(length):
            if buttons[row][column]["text"] == buttons[row + 1][column]["text"] != "":
                matches+=1
                indexes.append((row, column))
        if matches == length:
            indexes.append((row + 1, column))
            return True
        else:
            matches = 0
            indexes.clear()

    #  \ diagonal check
    for row, column in zip(range(length), range(length)):
            if buttons[row][column]["text"] == buttons[row + 1][column + 1]["text"] != "":
                matches+=1
                indexes.append((row, column))
    if matches == length:
        indexes.append((row + 1, column + 1))
        return True
    else:
        matches = 0
        indexes.clear()

    # / diagonal check
    for row, column in zip(reversed(range(length + 1)), range(length)):
            if buttons[row][column]["text"] == buttons[row - 1][column + 1]["text"] != "":
                matches+=1
                indexes.append((row, column))
    if matches == length:
        indexes.append((row - 1, column + 1))
        return True
    else:
        matches = 0
        indexes.clear()

    # BOTH DIAGONAL CHECKS AREN'T UNIVERSAL YET, WORKS ONLY FOR 3 X 3 BOARD
    
    if empty_spaces() is False:
        for row in range(len(buttons)): 
            for column in range(len(buttons[0])):
                buttons[row][column].config(bg="yellow")
        return "Tie"
    
    return False

def empty_spaces():
    length = len(buttons)
    for row in range(length):
        for column in range(length):
            if buttons[row][column]["text"] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(len(buttons)):
        for column in range(len(buttons[0])):
            buttons[row][column].config(text = "", bg = "#F0F0F0")



window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
board_size = 3

buttons = [[0 for i in range(board_size)] for j in range(board_size)]

label = Label(text=player + " turn", font=("Blambot Pro Lite", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=("Blambot Pro Lite", 20), command=new_game)
reset_button.pack()

frame = Frame(window)
frame.pack()

for row in range(len(buttons)):
    for column in range(len(buttons[0])):
        buttons[row][column] = Button(frame, text="", font=("consolas", 40), width=5, height=2,
                                      command= lambda row=row, column = column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()