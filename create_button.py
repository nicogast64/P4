from calendar import c
from smtplib import LMTP
from socket import fromshare
from tkinter import Button, Canvas
#from tkinter.tix import TList
from tkinter import ttk
import PIL.Image
import PIL.ImageTk
from create_window import *
from array import *
from game_management import *
from functools import partial
from game_management import fill_column
from game_management import restart_game

bg_color = "#25CFD4"



def create_circle_tab(win):
    w = 700
    h = 600
    p_x = 20
    p_y = 20
    line = []*7
    tab = []*6
    canvas = Canvas(win, width=w, height=h,bg="#2555D4", borderwidth=1, highlightthickness=2)
    for x in range(6):
        p_x= 20
        line.clear()
        for y in range(7):
            circle = canvas.create_oval(p_x,p_y,p_x+60,p_y+60, fill=bg_color, )
            p_x += 100
        p_y+= 100
    return canvas

def create_button_line(win, tab_canvas):
    w = 700
    h = 150
    p_x = 10
    p_y = 10
    line = []*7
    raw_blue_button = PIL.Image.open("blue_button.png")
    resized_blue_button = raw_blue_button.resize((80,80))

    canvas = Canvas(win, width=w, height=h, bg=bg_color, borderwidth=0, highlightthickness=0)
    blue_button= PIL.ImageTk.PhotoImage(master=canvas, image=resized_blue_button)
    canvas.image = blue_button
    for x in range(7):
        Button(canvas, image=blue_button,bg=bg_color, borderwidth=0, activebackground=bg_color, command=partial(fill_column,tab_canvas,x)).place(x=p_x, y=p_y)
        p_x += 100

    return canvas


def create_restart_button(win, tab_canvas):
    w = 300
    h = 150
    frame = Frame(win, bg=bg_color,width=w, height=h, borderwidth=0)
    Button(frame, text="RESTART",command=partial(restart_game, tab_canvas), borderwidth=0, bg = "green", fg = "black" ).pack(pady=30, fill=X)
    frame.place(x=1300, y=1000)
