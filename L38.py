# Inner Function

def outer():
    print("In outer function")

    def inner( num ):
        print("In inner function", num)

    return inner

something = outer()
print(something)
something(5)

# Class Homework
print()
def greet():

    def message():
        print("Welcome to Python!")

    message()

greet()
