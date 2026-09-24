# Factorial of Number using recursion

import sys
from time import sleep

print("Maximum limit of recursive function:", end=" ")
print(sys.getrecursionlimit())

# changing the limit of recursive function
sys.setrecursionlimit(1001)

print("Now maximum limit of recursive function:", end=" ")
print(sys.getrecursionlimit())

count = 1
def greet():
    global count
    print("Hello", count)
    count = count + 1
    sleep(0.05)
    # greet()
greet()

# Class Homework 

# print numbers from 1 to 10 using recursion

n = 1
def numbers():
    global n
    if n > 10:
        return
    print(n, end = " ")
    n += 1
    numbers()
numbers()