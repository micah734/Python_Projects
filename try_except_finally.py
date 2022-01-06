

def getInfo():
    x=input("\n Please input a number.")
    y=input("\n Please select another number.")
    return x,y

def multiply():
    go=True
    while go:
        x,y=getInfo()
        try:
            z=int(x)*int(y)
            go=False
        except ValueError:
            print("\n You did not give an integer, please try again.")
    
    print("{} times {} equals {}.".format(x,y,z))     
                  



if __name__ == "__main__":
    multiply()
