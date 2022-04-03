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
frame = None

def display_token_color(win, token_color_text):
    global token_color
    global frame
    if frame != None:
        frame.destroy()
    frame = Frame(win, bg=bg_color)
    token_color_frame = Label(frame, textvariable=token_color_text, bg=bg_color, fg=token_color, font=("Tahoma", 40))

    token_color_frame.pack()
    frame.place(x=150,y=500)

def edit_token_color(win):
    global token_color
    token_color_text = StringVar(value="default value")
    token_color_text.set("Player "+token_color)
    display_token_color(win, token_color_text)

def fill_column(win,canvas,nb_col):
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
            print(game_tab[(7*x)+nb_col])
    canvas.place(x=610, y=200)

    return canvas
   
def restart_game(canvas):
    global game_tab
    game_tab = ["vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide","vide"]
    for x in range(42):
        canvas.itemconfig(x, fill=bg_color)
    canvas.place(x=610, y=200)


