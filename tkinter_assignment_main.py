# Python Ver:   3.8.2
#
# Author:       Kevin McCrea   
#
# Purpose:      Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:

from tkinter import *
import tkinter as tk


# Be sure to import our other modules
# so we can have access to them
import tkinter_assignment_gui


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(700,700) #(Width, Height)
        self.master.maxsize(700,700)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")

        # load in the GUI widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        tkinter_assignment_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


































