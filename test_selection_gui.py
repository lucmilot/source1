# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 08:41:40 2018

@author: XT21586
"""
from tkinter import Tk
from tkinter import Button
from tkinter import Listbox
import tkinter

master=tkinter.Tk()

label=tkinter.Label(master, text="Python Lake: Simple Widget"). pack()
button=tkinter.Button(master, text="Submit").pack()
checkbox=tkinter.Checkbutton(master, text="CheckBox").pack()
listbox=tkinter.Listbox(master).pack()

master.mainloop()

master.destroy()