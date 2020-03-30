# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:25:44 2018

@author: XT21586
"""

try:
  import Tkinter              # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk

import time


def testluc():
    print ( "xxx" )

MAX = 10
ke = 0
ke_max = 3

prog_bar = Tkinter.Tk()
prog_bar.geometry('{}x{}'.format(400, 100))
progress_var = DoubleVar() #here you have ints but when calc. %'s usually floats
theLabel = Label(prog_bar, text="Sample text to show")
theLabel.pack()
progressbar = ttk.Progressbar(prog_bar, variable=progress_var, maximum=MAX)
progressbar.pack(fill=X, expand=1)


def loop_function():
    global ke
    ke += 1
    if ke > ke_max : 
        prog_bar.destroy()
    k = 0
    while k <= MAX:
    ### some work to be done
        progress_var.set(k)
        k += 1
        time.sleep(0.1)
        
        testluc()
        
        prog_bar.update_idletasks()
    prog_bar.after(100, loop_function)

loop_function()
prog_bar.mainloop()