def add():
    a = 5
    b = 4
    c = a + b
    print(c)

# call add block
add()

def add(x,y):
    a = x
    b = y
    c = a + b
    print(c)

# call add block
add(2,3)

def add(x,y):
    """ Adds two values """  #adds a brief description about the defined function
    a = x
    b = y
    c = a + b
    return c

# call add block
result = add(8,6)
print("Result is:",result)

result = add(8,5)
print("Result is:",result)