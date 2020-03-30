from tkinter import *
 

#txt.focus()
#txt = Entry(window,width=10, state='disabled')

def clicked():
    global buf1
    res = "Welcome to " + txt.get()
    buf1 = txt.get()
    lbl.configure(text= res)
    #window.quit()
    window.destroy()

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
 
lbl = Label(window, text="Hello", font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

btn = Button(window, text="Click Me", bg="orange", fg="red",  command=clicked)
btn.grid(column=2, row=0)

window.mainloop()

print (buf1)

'''
    root = tk.Tk()
    username = "root"
    password = "admin"
    app = App(root)
    app.mainloop()
'''