# Anonymous Function / Lambda Function
# Function without a name

def fun(num):
    return num * num
# we can also assign a function to some other identifier
square = fun

# declaring lambda funtion
func = lambda num : num * num

result = square(5)
print(result)
print(func(6))

add = lambda a, b : a + b

print(add(5, 6))


# Class Homework

funcc = lambda num : print("Even") if (num % 2 == 0) else print("Odd")
funcc(int(input("Enter a number:")))