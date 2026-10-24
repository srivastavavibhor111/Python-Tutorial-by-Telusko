# Object Oriented Programming
# Class and Object
class computer:

    def __init__(self, cpus, ram, ssd):
        print("init called")
        self.cpus = cpus
        self.ram = ram 
        self.ssd = ssd

    #class variable 
    cpu = "i5"

    def config(self):
        print("config :", self.cpus, self.ram, self.ssd)

com1 = computer("i4", "6GB", "1TB")
print(type(com1))

com1.cpu = "i6"

print(com1.cpu)
print(com1.cpus)

com2 = computer("i5", "96GB", "2TB")
com2.config()

#Homework
class Device:
    def __init__(self, name):
        print("Init called for", name)
        self.name = name.upper()

    def show(self):
        print("Device:", self.name)

d1 = Device("laptop")
d2 = Device("mobile")

d1.show()
d2.show()