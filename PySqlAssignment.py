

import sqlite3 #imported sqlite


conn=sqlite3.connect('assignment.db') #named and created the database


with conn: #creating the table to input the data
    cur=conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS tbl_assignment(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        fileList TEXT)")
    conn.commit()
conn.close()

fileList=('information.docx','Hello.txt','myImage.png',\
              'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn=sqlite3.connect('assignment.db')

for x in fileList: #finding .txt files to add to the db and then printing them
    if x.endswith('.txt'):
        with conn:
            cur=conn.cursor()
            cur.execute("INSERT INTO tbl_assignment(fileList) VALUES (?)",(x,))
            displayx='The following files where added to the database: \n{}'.format(x,)
            print(displayx)
            
