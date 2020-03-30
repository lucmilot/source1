# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:17:14 2018

@author: XT21586
"""
import tkinter
from tkinter import messagebox
 
# hide main window
root = tkinter.Tk()
root.withdraw()
 
# message box display
messagebox.showerror("Error", "Error message")
messagebox.showwarning("Warning","Warning message")
messagebox.showinfo("Information","Informative message")

print ('DONE')