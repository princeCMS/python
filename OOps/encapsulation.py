class Person:
    def __init__(self,name,age):
        self.name = name  # public
        self.__age = age  # private 

    # normal method 
    # getter method()
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.__age
    
    # setter method()
    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.__age = age

p1 = Person('Prince',20)
print(p1.name)
# print(p1.__age)  we cant access private properties directly

# get private properties
print(p1.getName())
print(p1.getAge())

# set private properties
p1.setName('Prince Singla')
p1.setAge(21)

# Now check is really data changes in normal and private properties
print(p1.getName())
print(p1.getAge())

