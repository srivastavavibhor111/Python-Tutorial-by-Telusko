# Talking about Arguments

# Positional/Required Arguments
print("Positional/Required Arguments")
def add(num1, num2):
    return num1 + num2
result = add(3, 5)
print(result)

# Default Arguments
print()
print("Default Arguments")
def add(num1, num2 = 0):
    return num1 + num2
result = add(3)
print(result)

def add(num1, num3, num4, num2 = 0):        #default values is always given at the end of all formal parameters
    return num1 + num2 + num3 + num4
result = add(3, 5, 6, 6)
print(result)

# Variable Length Arguments
print()
print("Variable Length Arguments")
def add(num1, *num2):
    sum = num1
    for i in num2:
        sum += i

    return sum

result = add(3, 5, 6, 6)
print(result)

# Keyword Arguments
print()
print("Keyword Arguments")
def person(name, age):
    print("Name: ", name)
    print("Age: ", age)

person(age=34, name="Navin")

# Keyword Variable Length Arguments
print()
print("Keyword Variable Length Arguments")
def person(name, **kwlargs):
    print("Name: ", name)
    for k, v in kwlargs.items():
        print(k, ":", v)

person(age=34, name="Navin", loc="Pune", tech="Python")