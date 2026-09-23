# Global vs Local Scope

a = 10 
print("Before using global function")
def something():
    a = 15
    print("Inside Function:", a)

something()
print("Outside Function:", a)
print()


a = 10 
print("Before using any function")
print("a : ", a)
print("After using global function")
def something():
    print(globals())
    print()
    print(globals()['a'])

    globals()['a'] = 20

    # global a
    a = 15
    print("Inside Function:", a)

something()
print("Outside Function:", a)