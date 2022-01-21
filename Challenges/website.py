
import webbrowser

import website_gui

f=open("webbrowser2.html","w")
f.write("<html><body><h1> {} </h1></body></html>".format(getBody)
f.close()

url='file:/Users/admin/Documents/GitHub/Python_Projects/Challenges/webbrowser2.html'
webbrowser.open_new_tab(url)


