from  tkinter import *
import tkinter as tk


import gui_main, gui_func
        

def load_gui(self):

    self.txt_browse=tk.Entry(self.master)
    self.txt_browse.grid(row=0,column=1, columnspan=3, pady=(10,0))
    self.txt_browse2=tk.Entry(self.master)
    self.txt_browse2.grid(row=1,column=1,columnspan=3,pady=(10,0))

    self.btn_browse=tk.Button(self.master,text='Browse...',command=lambda:gui_func.callback(self))
    self.btn_browse.grid(row=0,column=0,pady=(10,0))
    self.btn_browse2=tk.Button(self.master,text='Browse...',command=lambda:gui_func.callbackdst(self))
    self.btn_browse2.grid(row=1,column=0,pady=(10,0))
    self.btn_check=tk.Button(self.master,text='Check for files...',command=lambda:gui_func.compare(self))
    self.btn_check.grid(row=3,column=0,ipady=(5))
    self.btn_close=tk.Button(self.master,text='Close Program')
    self.btn_close.grid(row=3,column=3,ipady=(5),sticky=SE)
    
        
if __name__ == "__main__":
    pass
