from tkinter import *
import tkinter as tk
from tkinter import messagebox

import webbrowser

import website_gui, website_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)
    
        self.master=master
        self.master.title("New Body of Website")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW",lambda:website_func.ask_quit(self))
        arg=self.master
        
        website_gui.load_gui(self)
    


if __name__ == "__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
    
