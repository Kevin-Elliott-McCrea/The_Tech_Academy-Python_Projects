
from tkinter import *
from tkinter import filedialog
import tkinter as tk

import tkinter_assignment_directory_main


    
def selectFolder(self):
    folder_path = filedialog.askdirectory()
    self.txt_browse1.insert(0,folder_path)



if __name__ == "__main__":
    pass
