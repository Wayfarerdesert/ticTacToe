from tkinter import *
import random


def next_turn():
    pass


def check_winner():
    pass


def empty_spaces():
    pass


def new_game():
    pass


window = Tk()
window.title("tic-tac-toe")
window.resizable(False, False)
# Set window size
window.geometry("600x650")

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=("consolas", 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=("consolas", 40),
            width=5,
            height=2,
            command=lambda row=row, column=column: next_turn(row, column),
        )
        buttons[row][column].grid(row=row, column=column)


window.mainloop()
