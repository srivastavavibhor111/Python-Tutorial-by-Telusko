# init and super method with Inheritance

class A:

    def __init__(self):
        print("in A __init__")

    def f1(self):
        print("f1 works")

class B(A):

    def __init__(self):
        super().__init__()
        print("in B __init__")
    
    def f2(self):
        super().f1()
        self.f1()
        print("f2 works")

obj1 = B()
obj1.f2()