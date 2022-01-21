from tkinter import *
import tkinter as tk
from tkinter import messagebox

import website_main, website_func

def load_gui(self):
    self.lbl_body=tk.Label(self.master,text='Input the body of the website to create: ') #Label
    self.lbl_body.grid(row=0,column=0,padx=(10,0),pady=(10,0))
    
    self.txt_body=tk.Text(self.master)#Box to input the information for the website
    self.txt_body.grid(row=1,column=0,rowspan=5, columnspan=3)
    
    self.btn_run=tk.Button(self.master,text="Create Website", command=lambda:website_func.build(self))
    self.btn_run.grid(row=7,column=0,pady=(10,0))

    self.btn_clear=tk.Button(self.master,text="Clear",command=lambda:website_func.clear(self))
    self.btn_clear.grid(row=7,column=0,pady=(10,0),sticky=SW)

    self.btn_close=tk.Button(self.master,text="Close",command=lambda:website_func.ask_quit(self))
    self.btn_close.grid(row=7,column=0,pady=(10,0),stick=SE)

#if __name__ == "__main__":
    
