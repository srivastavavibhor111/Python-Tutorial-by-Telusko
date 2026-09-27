# Decorators in Python

def log_deco(func):
    def wrap(*args):
        print("values ", args)
        result = func(*args)
        return result
    return wrap

def greater_first(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return wrap

@log_deco
@greater_first
def sub(a, b):
    return a - b

@log_deco
@greater_first
def divide(a, b):
    return a/b

@log_deco
def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

result1 = divide(2,4)
print("Result1=", result1)

result2 = sub(2,4)
print("Result2=", result2)

result3 = add(3,4,5,6)
print("Result3=", result3)


# Class Homework
def logger(func):
    def wrap():
        print("This is a decorator")
        return wrap()
    return func

@logger
def greet():
    print("Hello, Python!")

greet()