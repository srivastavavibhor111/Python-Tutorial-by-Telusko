# Array Functions

from array import *

arr1 = array('i', [33,4,55,5,66])
print("Before Appending:")
print(arr1)
# append()
arr1.append(44)
print("After Appending:")
print(arr1)

arr1.reverse()
print("After Reversing:")
print(arr1)

# Copying an array 
print("Copying arrays")
print()
# Method 1
print("Method 1")
arr1 = array('i', [33,4,55,5,66])
arr2 = arr1
print("arr1 = ", arr1, "id =", id(arr1))
print("arr2 = ", arr2, "id =", id(arr2))
print("Since id of both is same, this method does not creates a copy in reality")

print()
# Method 2
print("Method 2")
arr1 = array('i', [33,4,55,5,66])
arr2 = array('i', arr1.tolist())
print("arr1 = ", arr1, "id =", id(arr1))
print("arr2 = ", arr2, "id =", id(arr2))
print("Since id of both is different, this method creates a copy in reality")

print()
# Method 3
print("Method 3")
arr1 = array('i', [33,4,55,5,66])
arr2 = array(arr1.typecode, arr1.tolist())
print("arr1 = ", arr1, "id =", id(arr1))
print("arr2 = ", arr2, "id =", id(arr2))
print("Since id of both is different, this method creates a copy in reality")