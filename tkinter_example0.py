
from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.mainloop()

 




from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
window.mainloop()




from tkinter import *
 
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)


def clicked():
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", bg="orange", fg="red",  command=clicked)
btn.grid(column=2, row=0)

window.mainloop()





from tkinter import *
 
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)
#txt.focus()
#txt = Entry(window,width=10, state='disabled')

def clicked():
    global buf1
    res = "Welcome to " + txt.get()
    buf1 = txt.get()
    lbl.configure(text= res)
    window.destroy


btn = Button(window, text="Click Me", bg="orange", fg="red",  command=clicked)
btn.grid(column=2, row=0)

window.mainloop()

print (buf1)



from tkinter import *
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app") 
window.geometry('350x200')
 
combo = Combobox(window)
combo['values']= (1, 2, 3, 4, 5, "Text")
combo.current(1) #set the selected item
combo.grid(column=0, row=0)
 
window.mainloop()



 