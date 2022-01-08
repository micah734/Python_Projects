

import os
import time

path='/Users/admin/Documents/GitHub/Python_Projects'

for file in os.listdir(path):
    print(file)


fname="Hello.txt"

fPath='/Users/admin/Documents/GitHub/Python_Projects'

abPath=os.path.join(fPath,fname)

print(abPath)


mod_time=os.path.getmtime(abPath)
print(mod_time)







import os
import time

path='/Users/admin/Documents/GitHub/Python_Projects'

f=""
t=0

def get_files:
    for file in os.listdir(path):
        f=os.path.join(path,file)
        if os.path.isfile(f):
            return(f)

def get_time:
    for f in os.listdir(path):
        t=os.path.getmtim(path):
            return(t)
        
for i in f:
    if i.endswith('.txt')
    print(i+f+t)



