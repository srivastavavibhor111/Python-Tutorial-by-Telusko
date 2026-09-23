# Array in Python

from array import *

arr1 = [ 33, 4, 55, 5, 66]
print(type(arr1))
print(arr1)

arr1 = array('i',[33, 4, 55, 5, 66])
print(type(arr1))
print(arr1)

for i in arr1:
    print(i)

print(arr1.tolist())
print(arr1.buffer_info())

# Homework Question

# Create a float array using the array module
l = [2.5, 4.8, -3.2, 6.7]

# Stores the values: 2.5, 4.8, -3.2, 6.7
arr2 = array('f', l)

# Iterating through the array and printing each element on a new line
print("Displaying all values of an array:")
for i in arr2:
    print(i)

# Now printing only postive numbers skipping negative numbers using continue
print("Displaying only the positive values of an array:")
for i in arr2:
    if i < 0:
        continue
    print(i)

