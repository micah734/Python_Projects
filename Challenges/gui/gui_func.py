from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
import  shutil
import os
import time


import gui_gui, gui_main



def callback(self):
    path=fd.askdirectory()
    self.txt_browse.delete(0,END)
    self.txt_browse.insert(0,path)
    return path


def callbackdst(self):
    pathdst=fd.askdirectory()
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0,pathdst)
    return pathdst


def compare(self):
    self.source1=self.txt_browse.get()
    self.recieving1=self.txt_browse2.get()
    self.files=os.listdir(self.source1)

    self.seconds_in_day=24*60*60

    now=time.time()
    before=now-self.seconds_in_day

    def last_mod_time(fname):
        return os.path.getmtime(self.source1_fname)

    for fname in self.files:
        self.source1_fname=os.path.join(self.source1,fname)
        if last_mod_time(self.source1_fname)>before:
            self.recieving_fname=os.path.join(self.recieving1,fname)
            shutil.move(self.source1_fname,self.recieving_fname)


