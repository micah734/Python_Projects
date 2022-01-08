import os
import time

path='/Users/admin/Documents/GitHub/Python_Projects'

f=""
t=0
i=""

def get_files():
    for file in os.listdir(path):
        f=os.path.join(path,file)
    return(f)   

def get_time():
    for f in os.listdir(path):
        t=os.path.getmtime(path)
    print(t)

def get_text():
    for i  in os.listdir(path):
        if i.endswith('.txt'):
            print(str(i)+str(f)+str(t))



if __name__ == "__main__":
    get_files()
    get_time()
    get_text()
