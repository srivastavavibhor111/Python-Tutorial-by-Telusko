a = 5
b = 6

print("Before Swapping")
print("a :",a)
print("b :",b)


# Method 1
c = a
a = b 
b = c
print("-----------Method 1-----------")
print("After Swapping")
print("a :",a)
print("b :",b)

# Method 2
a = 5
b = 6
a = a + b
b = a - b
a = a - b
print("-----------Method 2-----------")
print("After Swapping")
print("a :",a)
print("b :",b)

# Method 3
a = 5
b = 6
a = a ^ b
b = a ^ b
a = a ^ b
print("-----------Method 3-----------")
print("After Swapping")
print("a :",a)
print("b :",b)

# Method 4
a = 5
b = 6
a,b = b,a
print("-----------Method 4-----------")
print("After Swapping")
print("a :",a)
print("b :",b)


# Guess the output
str1 = "telusko"
str2 = "python"

str1, str2 = str2, str1

print("str1:", str1)
print("str2:", str2)