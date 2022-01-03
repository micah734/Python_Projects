

num1=6
key=True

if num1 == 12:
    if key:
        print('Num 1 is equal to Twelve  and they have  the key')
    else:
        print('Num 1 is equal to Twelve  and they have  do not have key')
elif  num1<12:
    print('Num 1 is less than tweleve')
else:
    print('Num 1 is not equal to twelve!')



if num1>5:
    if key:
        print('num1 is greater than 5 and has the key')
    else:
        print('num1 is greater than 5 but does not have a key')
elif num1==5:
    print('num1 is equal to 5')
else:
    print('num1 is less than 5')
    
print(bool(num1))
print(bool(key))
x=isinstance(5, str)
print(x)


i=0
for i in range(10):
    print("{} iteration through the loop.".format(i))
    i += 1
    

i=0
while i<10:
    print("{} iteration through the loop.".format(i))
    i += 1

i=0
while i<4:
    print("I like your face!")
    i +=1

i=1     
while i<9:
    print("My wife is wonderful!")
    if i==3:
        break
    i +=1

#Continue  Loop
i=1
while i<12:
    i +=1
    if i==4:
        continue
    print(i)


i=0
while i<5:
    print("My Name  is  Fred.")
    i+=1
else:
    print("My name is  not  Fred")



#For Loop

states=["Indiana","Missouri","Illinois","Texas"]
for x   in states:
    print(x)


#For Loop  with Break

for x in states:
    print(x)
    if  x=="Missouri":
        break


#For loop with  continue


for x in states:
    if x =="Illinois":
        continue
    print(x)


#For  Range

for  x in range(2):
    print(x)

for x in range(3,8):
    print(x)

#else function

for x  in range(4):
    print(x)
else:
    print("finally finished!")

