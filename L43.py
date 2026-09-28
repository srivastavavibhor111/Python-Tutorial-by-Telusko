# Object Oriented Programming
# Class and Object
class computer:

    def config(self):
        print("i7, 16GB, 1TB")

com1 = computer()
print(type(com1))

com2 = computer()
com3 = computer()

computer.config(com1)
computer.config(com2)

com1.config()

# Class Homework
class Laptop:

    def details(self, brand, ram):
        print("BrandName:", brand)
        print("RAM:", ram)

obj1 = Laptop()
obj2 = Laptop()

obj1.details("Dell", "16GB")
obj2.details("HP", "8GB")