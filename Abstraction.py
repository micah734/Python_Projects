from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
        
class Laptop(Computer):
    def process(self):
        print("its running")

class Programmer():
    def work(self):
        print("Solving bugs")
        com1.process()

com1=Laptop()
prog1=Programmer()
prog1.work()
