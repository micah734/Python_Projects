from tkinter import *
import tkinter as tk
from tkinter import messagebox

import student_gui
import student_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define our master frame configuration
        self.master=master
        self.master.minsize(800,500)
        self.master.maxsize(800,500)
        student_func.center_window(self,800,500)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW", lambda:student_func.ask_quit(self))
        arg=self.master

        student_gui.load_gui(self)

if __name__ == "__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
