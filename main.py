from tkinter import *
import random


def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            buttons[row][column]["fg"] = player_1

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " Wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
        else:
            buttons[row][column]["text"] = player
            buttons[row][column]["fg"] = player_2

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " Wins"))

            elif check_winner() == "Tie":
                label.config(text=("Tie!"))


def check_winner():
    # Check rows
    for row in range(3):
        if (
            buttons[row][0]["text"]
            == buttons[row][1]["text"]
            == buttons[row][2]["text"]
            != ""
        ):
            buttons[row][0].config(bg=win_bg)
            buttons[row][1].config(bg=win_bg)
            buttons[row][2].config(bg=win_bg)
            return True

    # Check columns
    for column in range(3):
        if (
            buttons[0][column]["text"]
            == buttons[1][column]["text"]
            == buttons[2][column]["text"]
            != ""
        ):
            buttons[0][column].config(bg=win_bg)
            buttons[1][column].config(bg=win_bg)
            buttons[2][column].config(bg=win_bg)
            return True

    # check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg=win_bg)
        buttons[1][1].config(bg=win_bg)
        buttons[2][2].config(bg=win_bg)
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg=win_bg)
        buttons[1][1].config(bg=win_bg)
        buttons[2][0].config(bg=win_bg)
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg=tie_bg)
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#ECECEC")


window = Tk()
window.title("tic-tac-toe")
window.resizable(False, False)
# Set window size
window.geometry("550x600")

win_bg = "green"
tie_bg = "yellow"
player_1 = "blue"
player_2 = "darkorange"
main_bg = "#F5EECB"
resetBtn_bg = "#CDBB60"

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create a frame to contain the label and reset button
top_frame = Frame(window, bg=main_bg)
top_frame.pack(side="top")

label = Label(top_frame, text=player + " turn", font=("consolas", 40), bg=main_bg)
label.pack(side="left")

# Add a spacer label for wider space
spacer_label = Label(top_frame, width=12, bg=main_bg)
spacer_label.pack(side="left")

reset_button = Button(
    top_frame, text="restart", font=("consolas", 20), command=new_game, bg=resetBtn_bg
)
reset_button.pack(side="right")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(
            frame,
            text="",
            font=("consolas", 40),
            width=4,
            height=2,
            command=lambda row=row, column=column: next_turn(row, column),
        )
        buttons[row][column].grid(row=row, column=column)

# Set background color
window.configure(bg=main_bg)
window.mainloop()
