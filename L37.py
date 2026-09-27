from functools import reduce
# Map function & Reduce function

# Method 1
print("Through Method 1")
nums = [4, 2, 9, 7, 5, 1, 6, 8]
def is_even(n):
    return n % 2 == 0

def doubles(n):
    return n * 2

def sum_it(a, b):
    return a + b

evens = list(filter(is_even, nums))
doubles = list(map(doubles, evens))
sum = reduce(sum_it, doubles)

print("Evens", evens)
print("Doubles", doubles)
print("Total", sum)
print()

# Method 2
print("Through Method 2")
nums = [4, 2, 9, 7, 5, 1, 6, 8]

evens = list(filter(lambda n : n % 2 == 0, nums))
doubles = list(map(lambda n : n * 2, evens))
sum = reduce(lambda a,b : a + b, doubles)

print("Evens", evens)
print("Doubles", doubles)
print("Total", sum)
print()

# Class Homework
l = [2, 3, 4]

cube = list(map(lambda n : n ** 3, l))
sum = reduce(lambda a, b : a + b, cube)

print("Cube", cube)
print("Sum", sum)