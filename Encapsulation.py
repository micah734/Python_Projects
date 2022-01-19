



class cars():
    def __init__(self):
        self.__brand="Chevy"
        self.model="Equinox"

obj=cars()
obj.__brand="Chevy"
print(obj.__brand)


class computers():
    def __init__(self):
        self._type="apple"

    def getType(self):
        print(self._type)

    def setType(self,private):
        self._type=private

obj=computers()
obj.getType()
obj.setType("Apple")
obj.getType()
