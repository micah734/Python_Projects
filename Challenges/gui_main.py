from  tkinter import *
import tkinter as tk

import gui_gui,gui_func

class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master=master
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol("WM_DELETE_WINDOW")
        arg=self.master

        gui_gui.load_gui(self)

if __name__ == "__main__":
    root=tk.Tk()
    App=ParentWindow(root)
    root.mainloop()
