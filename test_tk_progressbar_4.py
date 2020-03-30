# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:25:44 2018

@author: XT21586
"""

#from ttk import Progressbar
from  tkinter.ttk import Progressbar

import tkinter as Tkinter


root = Tkinter.Tk()
root.geometry('400x30+10+50')
    
value_progress =50
root.title("Progressbar Thingymawhatsit")
root.config(bg = '#F0F0F0')  

canvas = Tkinter.Canvas(root, relief = Tkinter.FLAT, background = "#D2D2D2",
                                            width = 400, height = 20)
            
            
progressbar = Progressbar(canvas, orient=Tkinter.HORIZONTAL,
                                  length=400, mode="indeterminate",
                                  variable=value_progress,
                                  )

canvas.create_window(1, 1, anchor=Tkinter.NW, window=progressbar)
canvas.grid()

root.mainloop()


