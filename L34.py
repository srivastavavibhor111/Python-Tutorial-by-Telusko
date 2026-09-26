# Higher Order Function - a function is called inside another function

def square(num):
    return num * num

def cube(num):
    return num * num * num

def operate(num, operation):
    return operation(num)

def operates(nums, operations):
    for i in nums:
        print(operations(i))

value = 5
print(operate(value, square))

values = [5, 6, 7]
operates(values, cube)

# Class Homework

def hof(l, funct):
    for i in l:
        print(funct(i), end=" ")

l_values = [1, 2, 3, 4, 5]
print("Square of", l_values, "are:")
hof(l_values, square)

