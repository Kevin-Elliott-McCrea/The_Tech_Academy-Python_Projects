

from tkinter import *
import tkinter as tk


import tkinter_assignment_gui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(520,200) #(Width, Height)
        self.master.maxsize(520,200)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        # load in the GUI widgets from a separate module,
        tkinter_assignment_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


































