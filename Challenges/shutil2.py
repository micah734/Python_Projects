import  shutil
import os
import time


source1='/Users/admin/Desktop/FolderB/'
recieving='/Users/admin/Desktop/FolderA/'
files=os.listdir(source1)

seconds_in_day=24*60*60

now=time.time()
before=now-seconds_in_day

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in files:
    source1_fname=os.path.join(source1,fname)
    if last_mod_time(source1_fname)>before:
        recieving_fname=os.path.join(recieving,fname)
        shutil.move(source1_fname,recieving_fname)
        
