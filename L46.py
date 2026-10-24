# Types of Methods in Python
class computer:

    #class variable 
    cpu = "i5"
    brand = "Telusko AI"

    def __init__(self, cpus, ram, ssd):
        print("init called")
        self.cpus = cpus
        self.ram = ram 
        self.ssd = ssd

    def config(self):
        print("config :", self.cpus, self.ram, self.ssd)

    @classmethod
    def info(cls):
        return cls.brand

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

com1 = computer("i4", "6GB", "1TB")
print(com1.brand)
print(computer.brand)

print(com1.info())

print(com1.gb_to_bytes(16))