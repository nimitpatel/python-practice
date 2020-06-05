'''
Explain steps to create widgets.
Write Python program to display a label on clicking a push button.
'''

from tkinter import *

tk = Tk()

def labelCallBack():
    Lb = Label(tk, text = "I'm a Label")
    Lb.pack()

Btn =  Button(tk, text = "Click me!", command = labelCallBack)

Btn.pack()
tk.mainloop()
