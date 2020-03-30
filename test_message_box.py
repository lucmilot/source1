# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:17:14 2018

@author: XT21586
"""
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("100x100")
def hello():
   messagebox.showinfo("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()