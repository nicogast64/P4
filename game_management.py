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

def fill_column(canvas,nb_col):
    global token_color
    global token_played
    global game_tab
    token_played = FALSE
    print(nb_col)
    for x in range(5,0,-1):
        if game_tab[(7*x+nb_col)] == "vide" and (token_played == FALSE):
            print("Numero de cercle : ", (7*x+nb_col+1))
            canvas.itemconfig((7*x+nb_col+1), fill=token_color)
            game_tab[(7*x+nb_col)] = token_color
            if token_color == "yellow":
                token_color = "red"
            else:
                token_color = "yellow"
            token_played = TRUE
            print(game_tab[(7*x)+nb_col])

    canvas.place(x=610, y=200)

    return canvas
   
def restart_game(canvas):
    global game_tab
    game_tab = ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]
    for x in range(42):
        canvas.itemconfig(x, fill=bg_color)
    canvas.place(x=610, y=200)