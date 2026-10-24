# Inheritance and MRO in python

# Single Level Inheritance
class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

class B(A):
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")

obj1 = B()
obj1.f1()

# Multilevel Level Inheritance
class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

class B(A):
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")

class C(B):
    def f5(self):
        print("f5 works")

obj2 = C()
obj2.f1()


# Multiple Inheritance
class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")

    def show(self):
        print("in A show")

class B():
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")

    def show(self):
        print("in A show")

class C(A, B):
    def f5(self):
        print("f5 works")

    def show(self):
        print("in A show")

obj3 = C()
obj3.show()
