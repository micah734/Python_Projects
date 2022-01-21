from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk

import gui_gui
import gui_main



def callback():
    filename=fd.askdirectory()
    filename.set(filename)

