# Nested ifs

num = 6
salary = 5

if num % 2 == 0:
    print("Even")
    if salary > 5:
        print("Great Job")
    else:
        print("Better luck next time")
else:
    print("Odd")

print("Bye")