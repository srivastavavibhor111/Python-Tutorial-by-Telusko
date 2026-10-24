# Polymorphism and Duck Typing

class Laptop:       #Duck
    def build(self):
        print("Laptop Builds")

class Desktop:      #crow
    def build(self):
        print("Desktop builds")

class Tablet:
    def open_pdf(self):
        print("Opening PDF")

class Alien:
    def code(self, machine : Laptop):
        print("Alien Building..")
        machine.build()

asus_rog = Laptop()
beast = Desktop()
lenovo_tab = Tablet()

navin = Alien()
navin.code(asus_rog)
navin.code(beast)
# navin.code(lenovo_tab)


# Homework

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

class Trainer:
    def train(self, animal):
        print("Training started...")
        animal.sound()

d = Dog()
c = Cat()

t = Trainer()
t.train(c)