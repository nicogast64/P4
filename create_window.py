from tkinter import *

def create_window(width, height, title, bg_color , *args):
    win = Tk()
    win.title(title)
    win.geometry(width+"x"+height)
    win.iconbitmap(args[0])
    win.config(background=bg_color)

    return win
