# Factorial of Number

print("Method 1")
print("Using for loop")
n = int(input("Enter a number to find the factorial:"))
f = 1
for i in range(1, n+1):
    f *= i
print(n, "!", " = ", f,sep="")


print("Method 2")
print("Using while loop")
def fact(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res

result = fact(int(input("Enter a number to find the factorial:")))
print(result)