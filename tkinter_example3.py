import tkinter as tk

class CloseAfterFinishFrame1(tk.Frame):  # Diz que herda os parametros de Frame
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, master)  # Inicializa com os parametros acima!!
        tk.Label(self, text="Hi", font=("Arial", 16)).pack()
        self.button = tk.Button(self, text="I am ready",
                           command=self.CloseWindow, font=("Arial", 12))
        self.button.pack()
        self.pack()

    def CloseWindow(self):
        # disable the button so pressing <SPACE> does not call CloseWindow again
        self.button.config(state=tk.DISABLED)
        self.forget()
        CloseAfterFinishFrame2(self.master)

class CloseAfterFinishFrame2(tk.Frame):  # Diz que herda os parametros de Frame
    def __init__(self, master):
        tk.Frame.__init__(self, master)  # Inicializa com os parametros acima!!
        tk.Label(self, text="Hey", font=("Arial", 16)).pack()
        button = tk.Button(self, text="the End",
                           command=self.CloseWindow, font=("Arial", 12))
        button.pack()
        self.pack()

    def CloseWindow(self):
        root.quit()

root = tk.Tk()
CloseAfterFinishFrame1(root)
root.mainloop()