from smtplib import LMTP
from socket import fromshare
from textwrap import fill
from tkinter import *
#from tkinter.tix import TList
#from tkinter import ttk
from turtle import bgcolor, circle
import PIL.Image
import PIL.ImageTk
from xml.etree.ElementInclude import include
from create_window import create_window
from create_button import *
from game_management import *

bg_color = "#25CFD4"

win = create_window("1920", "1080", "Puissance 4", bg_color, "logo.ico")
#---------------------------------------------------- Game shape
frame = Frame(win, bg=bg_color)
app_title = Label(frame, text="Puissance 4", bg='yellow', fg='red', font=("Tahoma",40))
app_subtitle = Label(frame, text="Aligne 4 jetons, et c'est gagné !", bg='red', fg='yellow', font=("Tahoma",25))

canvas_grid = create_circle_tab(win)
canvas_button_bar = create_button_line(win, canvas_grid)
create_restart_button(win, canvas_grid)

app_title.pack()
app_subtitle.pack()
frame.pack()

canvas_grid.place(x=610, y=200)
canvas_button_bar.place(x=610, y=830)
win.mainloop()