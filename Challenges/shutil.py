import  shutil
import os
import os.pad,time


source='/Users/admin/Desktop/FolderA/'

destination='/Users/admin/Desktop/FolderB/'
files=os.listdir(source)

for i in files:
    shutil.move(source+i,destination)



