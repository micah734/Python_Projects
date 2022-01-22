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
    self.source1='{}'.format(path(self))
    self.recieving='{}'.format(pathdst(self))
    self.files=os.listdir(self.source1)

    self.seconds_in_day=24*60*60

    now=time.time()
    before=now-seconds_in_day

    def last_mod_time(fname):
        return os.path.getmtime(fname)

    for fname in files:
        self.source1_fname=os.path.join(self.source1,fname)
        if last_mod_time(self,source1_fname)>before:
            self.recieving_fname=os.path.join(self.recieving,fname)
            shutil.move(self.source1_fname,self.recieving_fname)


