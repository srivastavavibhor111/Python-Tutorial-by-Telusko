# While loop

i = 1
while i <= 5:
    print("Telusko", end = " ") 

    j = 1
    while j <= 4:
        print("Rocks!!", end = " ")
        j += 1

    i += 1
    print()

print(i)


# Class Homework

# To print all even numbers from 1 to 10
k = 1
print("Even Numbers from 1 to 10 are:")
while k <= 10:
    if (k % 2 == 0):
        print(k)
    k += 1