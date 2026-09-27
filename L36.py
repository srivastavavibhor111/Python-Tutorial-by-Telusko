# filter function in python

# Method 1
print("Through Method 1")
nums = [4, 2, 9, 7, 5, 1, 6, 8]

def is_even(n):
    return n % 2 == 0

evens = list(filter(is_even, nums))
print(evens)
print()

# Method 2
print("Through Method 2")
nums = [4, 2, 9, 7, 5, 1, 6, 8]

is_even = lambda n : n % 2 == 0

evens = list(filter(is_even, nums))
print(evens)
print()

# Method 3
print("Through Method 3")
nums = [4, 2, 9, 7, 5, 1, 6, 8]

evens = list(filter(is_even, nums))
print(evens)
print()

# Class Homework
print("Homework")
l = [10, 55, 32, 75, 90, 41, 68]

greater = list(filter(lambda n : n > 50, l))

print(greater)