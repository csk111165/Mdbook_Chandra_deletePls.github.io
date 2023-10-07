# This is class demo code

class Base():
    # constructor
    def __init__(self, name):
        self.name = name
    
    # print function
    def printMe(self):
        print(f"Just normal printing {self.name}")


# create an object of Base class
obj = Base("chandra")
obj.printMe()