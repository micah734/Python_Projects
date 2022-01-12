#creating a class

class CellPhone():
    brand="Unknown",
    storage=0,
    os="Unknown",
    screen_size=0

    def information(self):
        msg="\nBrand: {}, \nStorage: {}, \nOperating System: {} \nScreen Size: {} \nPassword:{}".format(self.brand,self.storage,self.os,self.screen_size,self.password)
        return msg


#child class

class Apple(CellPhone):
    brand="Apple",
    storage=256,
    os="ios 15.5",
    screen_size=6.7
    password="apple"

    def design(self):
        msg="\nApple creates such streamlined phones and operating systems!"
        return msg

class Android(CellPhone): #Using the same setup for  CellPhone just chinging pin_code to password
    brand="Samsung",
    storage=512,
    os="Android 12.0",
    screen_size=6.8,
    pin_code=3840

    def information(self):
        msg="\nBrand: {}, \nStorage: {}, \nOperating System: {} \nScreen Size: {} \nPassword:{}".format(self.brand,self.storage,self.os,self.screen_size,self.pin_code)
        return msg



if __name__ == "__main__":

    Apple=Apple()
    print(Apple.information())

    Android=Android()
    print(Android.information())
    
    
        
