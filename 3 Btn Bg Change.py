'''
Write Python GUI program to create three push buttons using Tkinter.
Background color of a frame should be changed when different buttons
are clicked.
'''

from tkinter import *

tk = Tk()

def red():
    f = Frame(tk, bg = "red", width = "100", height = "100")
    f.pack()
    
def green():
    f = Frame(tk, bg = "green", width = "100", height = "100")
    f.pack()
    
def blue():
    f = Frame(tk, bg = "blue", width = "100", height = "100")
    f.pack()

rBtn = Button(tk, text = "Red", command = red)
gBtn = Button(tk, text = "Green", command = green)
bBtn = Button(tk, text = "Blue", command = blue)

rBtn.pack()
gBtn.pack()
bBtn.pack()
tk.mainloop()
