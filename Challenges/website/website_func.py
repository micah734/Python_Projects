
import webbrowser
import os

import website_gui,website_main

def build(self):
    self.g=open("website1.html","w")
    self.g.write("<html><body><h1>{}</h1></body></html>".format(getBody(self)))
    self.g.close()
    
    self.url='website1.html'
    webbrowser.open_new_tab(self.url)


def getBody(self):
    userText=self.txt_body.get("1.0","end-1c")
    return userText
      

    
def clear(self):
    self.txt_body.delete("1.0","END")

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)



if __name__ == "__main__":
        pass
