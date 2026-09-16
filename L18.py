a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before Swapping")
print("a :",a)
print("b :",b)

# Method 4
a,b = b,a
print("-----------Method 4-----------")
print("After Swapping")
print("a :",a)
print("b :",b)

print("Addition pf a and b")
c = a + b
print(c)



# To print a single character from user input
print("-----------Method 1-----------")
s = input("Enter a character: ")
print(s)
print(s[0])

# below Method is invalid
# print("-----------Method 2-----------")
# s = char(input("Enter a character: "))
# print(s)

print("-----------Method 2-----------")
s = input("Enter a character: ")[0]
print(s)

# Video Question
# Display Students Information
stu_name = input("Enter Student's Name: ")
stu_rollno = int(input("Enter Student's Roll No: "))
print("Name: ", stu_name)
print("Roll No: ", stu_rollno)