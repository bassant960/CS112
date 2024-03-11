
from tkinter import *         #import tkinter to make GUI
import random

def next_turn(row, column):     #this function specify who player will play this turn
    global player
    if game_btns[row][column]['text'] == "" and not check_winner():
        game_btns[row][column]['text'] = player
        if player == players[0]:
            player = players[1]
        else:
            player = players[0]
        label.config(text=(player + " turn"))
        check_winner()

def check_winner():
    for row in range(3):     #check all horizontal conditions
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            highlight_winner(row, 0, row, 1, row, 2)
            return True
    for column in range(3):          #check all vertical conditions
        if game_btns[0][column]['text'] == game_btns[1][column]['text'] == game_btns[2][column]['text'] != "":
            highlight_winner(0, column, 1, column, 2, column)
            return True
        # check diagonal conditions for win
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        highlight_winner(0, 0, 1, 1, 2, 2)
        return True
    if game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        highlight_winner(0, 2, 1, 1, 2, 0)
        return True
    if not empty_squares():    # no empty squares means no winner
        highlight_nowinner()
        label.config(text="Tie: No winner")
        return True
    return False

def highlight_winner(r1, c1, r2, c2, r3, c3):
    game_btns[r1][c1].config(bg="green")
    game_btns[r2][c2].config(bg="green")
    game_btns[r3][c3].config(bg="green")
def highlight_nowinner():    # to color background of squares
    for row in range(3):
        for column in range(3):
            game_btns[row][column].config(bg="red")

def empty_squares():
    for row in range(3):
        for column in range(3):
            if game_btns[row][column]['text'] == "":
                return True
    return False

def play_again():    #called in restart button
    global player
    player = random.choice(players)
    label.config(text=(player + " turn"))
    for row in range(3):
        for column in range(3):    #to return the virtual color
            game_btns[row][column].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-tac-toe")

players = ["X", "O"]
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=(player + " turn"), font=('consolas', 40))
label.pack(side='top')

restart_btn = Button(text="Restart", font=('consolas', 28), command=play_again)
restart_btn.pack(side="top")

btns = Frame(window)
btns.pack()

for row in range(3):
    for column in range(3):
        game_btns[row][column] = Button(btns, text="", font=('consolas', 50), width=4, height=1,
                                        command=lambda row=row, column=column: next_turn(row, column))
        game_btns[row][column].grid(row=row, column=column)

window.mainloop()