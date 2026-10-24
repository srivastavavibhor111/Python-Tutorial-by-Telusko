#method overriding

class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

obj1 = B()
obj1.show()

#HomeWork
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")
        super().show()

obj = B()
obj.show()