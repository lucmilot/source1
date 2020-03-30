# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:25:44 2018

@author: XT21586
"""

#from ttk import Progressbar
from  tkinter.ttk import Progressbar

import tkinter as Tkinter

class Example(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        value_progress =50
        self.parent.title("Progressbar Thingymawhatsit")
        self.config(bg = '#F0F0F0')
        self.pack(fill = Tkinter.BOTH, expand = 1)
                #create canvas
        canvas = Tkinter.Canvas(self, relief = Tkinter.FLAT, background = "#D2D2D2",
                                            width = 400, height = 20)

        progressbar = Progressbar(canvas, orient=Tkinter.HORIZONTAL,
                                  length=400, mode="indeterminate",
                                  variable=value_progress,

                                  )
        # The first 2 create window argvs control where the progress bar is placed
        canvas.create_window(1, 1, anchor=Tkinter.NW, window=progressbar)
        canvas.grid()


def main():
    root = Tkinter.Tk()
    root.geometry('400x30+10+50')
    app = Example(root)
    app.mainloop()

if __name__ == '__main__':
    main()