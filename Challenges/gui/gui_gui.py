from  tkinter import *
import tkinter as tk


import gui_main, gui_func
        

def load_gui(self):

    self.txt_browse=tk.Entry(self.master,command=gui_func.callback)
    self.txt_browse.grid(row=0,column=1, columnspan=3, pady=(10,0))
    self.txt_browse2=tk.Entry(self.master,text="")
    self.txt_browse2.grid(row=1,column=1,columnspan=3,pady=(10,0))

    self.btn_browse=tk.Button(self.master,text='Browse...',command=gui_func.callback)
    self.btn_browse.grid(row=0,column=0,pady=(10,0))
    self.btn_browse2=tk.Button(self.master,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,pady=(10,0))
    self.btn_check=tk.Button(self.master,text='Check for files...')
    self.btn_check.grid(row=3,column=0,ipady=(5))
    self.btn_close=tk.Button(self.master,text='Close Program')
    self.btn_close.grid(row=3,column=3,ipady=(5),sticky=SE)
    
        
if __name__ == "__main__":
    pass
