

mySentence = 'loves the color'

color_list = ['red','blue','pink','teal' ,'black']

def color_function (name) :
    lst=[]
    for i in color_list:
        msg='{} {} {}' .format (name,mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go=True
    while go:
        name=input('What is your name?')
        if name=='':
            print('You need to provide  your name,')
        elif name=='Sally':
            print('Sally, you  may  not use this software')
        else:
            go=False
    lst=color_function(name)
    for i in lst:
        print(i)


get_name()



myCar=['chevy','ford','toyota']

def car_function(fname):
    lst=[]
    for i in myCar:
        car='{} drives a {}'.format(fname,i)
        lst.append(car)
    return lst


def get_fname():
    go=True
    while go:
        fname=input('What is your first name?')
        if fname=='':
            print('You need to provide your name.')
        else:
            go=False
        lst=car_function(fname)
        for i in lst:
            print(i)
    
get_fname()




computer=['apple','ibm','lenovo']

x=len(computer)
print(x)



for y in computer:
    print(y)

computer.sort(reverse=True)
print(computer)


computer.append('apple')
z=computer.count('apple')
print(z)


#Lambda function

x=lambda a: a+45
print(x(900))


    
        
#
#lst=color_function ('Sally')
#for i in lst:
#    print(i)
