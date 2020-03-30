# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 09:25:44 2018

@author: XT21586
"""

import tkinter as tk   # Python 3
import tkinter.ttk as ttk
  
from queue import Queue 
    
import threading
import time

queue1 = Queue()

root = tk.Tk()
#s = tk.Style()
#s.theme_use("default")
#s.configure("TProgressbar", thickness=50)


frame1 = tk.Frame(root)
frame1.pack()

canvas1 = tk.Canvas(frame1, bg="blue", height=15, width=500)
canvas1.pack()

#root.mainloop()




# Function to do 'stuff' and place object in queue for later #
def foo():
    # sleep to demonstrate thread doing work #
    time.sleep(12)
#    obj = [x for x in range(0,10)]
#    queue1.put(obj)

# Create thread object, targeting function to do 'stuff' #
thread1 = threading.Thread(target=foo, args=())

# Function to check state of thread1 and to update progressbar #
def progress(thread, queue):
    # starts thread #
    thread.start()

    # defines indeterminate progress bar (used while thread is alive) #
    pb1 = ttk.Progressbar(canvas1, style="TProgressbar")

    # defines determinate progress bar (used when thread is dead) #
    pb2 = ttk.Progressbar(canvas1, style="TProgressbar")
    pb2['value'] = 100

    # places and starts progress bar #
    pb1.pack()
    pb1.start()

    # checks whether thread is alive #
    while thread.is_alive():
        root.update()
        pass

    # once thread is no longer active, remove pb1 and place the '100%' progress bar #
    pb1.destroy()
    
    pb2.pack()
    time.sleep(2)
    pb2.destroy()
    root.destroy()
    
    # retrieves object from queue #
    #work = queue.get()
    work = 'tata'
    return work

work = progress(thread1, queue1)
root.mainloop()