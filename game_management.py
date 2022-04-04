from operator import is_
from smtplib import LMTP
from socket import fromshare
from tkinter import *
#from tkinter.tix import TList
#from tkinter import ttk
from turtle import bgcolor, circle
import PIL.Image
import PIL.ImageTk
from xml.etree.ElementInclude import include
from create_window import create_window
from create_button import *
import time

bg_color = "#25CFD4"
token_color = "red"
token_played = FALSE

game_tab = ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]
frame_player = None
frame_winner = None
label_winner = None
line_data = []
lines = []
column_data =[]
columns = []
activate_full_column = TRUE

def display_token_color(win, token_color_text):
    global token_color
    global frame_player
    if frame_player != None:
        frame_player.destroy()
    frame_player = Frame(win, bg=bg_color)
    token_color_frame = Label(frame_player, textvariable=token_color_text, bg=bg_color, fg=token_color, font=("Tahoma", 40))

    token_color_frame.pack()
    frame_player.place(x=150,y=500)

def edit_token_color(win):
    global token_color
    token_color_text = StringVar(value="default value")
    token_color_text.set("Player "+token_color)
    display_token_color(win, token_color_text)

def fill_column(win,canvas,nb_col):
    if activate_full_column == TRUE:
        global token_color
        global token_played
        global game_tab
        token_played = FALSE
        for x in range(5,-1,-1):
            if game_tab[(7*x+nb_col)] == "vide" and (token_played == FALSE):
                canvas.itemconfig((7*x+nb_col+1), fill=token_color)
                game_tab[(7*x+nb_col)] = token_color
                
                if token_color == "yellow":
                    token_color = "red"
                else:
                    token_color = "yellow"
                edit_token_color(win)
                token_played = TRUE
        canvas.place(x=610, y=200)
        check_line(win)

        return canvas
   
def restart_game(canvas):
    global game_tab
    global frame_winner
    global label_winner
    global activate_full_column
    game_tab = ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]
    for x in range(0,42,1):
        canvas.itemconfig(x+1, fill=bg_color)
    canvas.place(x=610, y=200)
    if frame_player != None:
        frame_winner.destroy()
    activate_full_column=TRUE

def find_connect(lines):        
    winner = ""
    for line in lines:
        for i in range(len(line)):
            if i+3 < len(line):
                if line[i] != "vide" and line[i+1] != "vide" and line[i+2] != "vide" and line[i+3] != "vide":    
                    if line[i]==line[i+1] and line[i] == line[i+2] and line[i] == line[i+3]:
                        winner = line[i]

    return winner

def find_horizontal_line():
    global lines
    global line_data
    lines.clear()
    for i in range(0,42,1):
        line_data.append(game_tab[i])
        if (i+1)%7 == 0:
            lines.append(line_data)
            line_data = []
    
    winner = find_connect(lines)

    return winner
                        

def find_vertical_line():
    global columns
    global column_data
    columns.clear()
    for i in range(0,7,1):
        for j in range(i,42,7):
            column_data.append(game_tab[j])
        columns.append(column_data)
        column_data =[]

    winner = find_connect(columns)
    return winner
    

def diagonal_type1(lines):
    winner = ""
    for i in range(0,3,1):
        for j in range(0,4,1):
            """
            if (i+3) <= len(lines) and (j+3) < len(lines[0]):
                if lines[i][j] != "vide" and lines[i+1][j+1] != "vide" and lines[i+2][j+2] != "vide" and lines[i+3][j+3] != "vide":
                    if lines[i][j] == lines[i+1][j+1] and lines[i][j] == lines[i+2][j+2] and lines[i][j] == lines[i+3][j+3]:
                        winner = lines[i][j]
            """ 
            if lines[i][j] != "vide":
                if lines[i+1][j+1] != "vide":
                    if lines[i+2][j+2] != "vide":
                        if lines[i+3][j+3] != "vide":
                            if lines[i][j] == lines[i+1][j+1] and lines[i][j] == lines[i+2][j+2] and lines[i][j] == lines[i+3][j+3]:
                                winner = lines[i][j]
    return winner

def diagonal_type2(lines):
    winner = ""
    for i in range(0,3,1):
        for j in range(3,7,1):
            if lines[i][j] != "vide":
                if lines[i+1][j-1] != "vide":
                    if lines[i+2][j-2] != "vide":
                        if lines[i+3][j-3] != "vide":
                            if lines[i][j] == lines[i+1][j-1] and lines[i][j] == lines[i+2][j-2] and lines[i][j] == lines[i+3][j-3]:
                                winner = lines[i][j]

    return winner

def find_diagonal_type1_line():
    global lines
    global line_data
    lines.clear()
    winner = ""
    for i in range(0,42,1):
        line_data.append(game_tab[i])
        if (i+1)%7 == 0:
            lines.append(line_data)
            line_data = []

    winner = diagonal_type1(lines)

    return winner

def find_diagonal_type2_line():
    global lines
    global line_data
    lines.clear()
    winner = ""
    for i in range(0,42,1):
        line_data.append(game_tab[i])
        if (i+1)%7 == 0:
            lines.append(line_data)
            line_data = []
    
    winner = diagonal_type2(lines)

    return winner

def is_a_winner(winner,win):
    global frame_winner
    global label_winner
    global activate_full_column
    frame_winner = Frame(win, bg=winner)
    if winner != "":
        if winner == "red":
            fg_color = "white"
        else:
            fg_color = "black"
        winner_txt = StringVar(value="default")
        winner_txt.set("Player "+winner+" win !")
        label_winner = Label(frame_winner, textvariable=winner_txt, bg=winner, fg=fg_color, font="Tahoma 50").pack(expand=YES)
        frame_winner.place(x=1400, y=500)
        activate_full_column = FALSE


def check_line(win):
    winner =""
    win_horiz = find_horizontal_line()
    win_vert = find_vertical_line()
    win_diag1 = find_diagonal_type1_line()
    win_diag2 = find_diagonal_type2_line()

    if win_horiz !="":
        winner = win_horiz
    elif win_vert != "":
        winner = win_vert
    elif win_diag1 != "":
        winner = win_diag1
    elif win_diag2 != "":
        winner = win_diag2
    else:
        winner = ""
    
    if winner !="":
        is_a_winner(winner, win)

   
   
    