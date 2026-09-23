# break and continue statements

print("Displaying numbers from 0 to 9:")
for j in range(10):
    print(j, end = " | ")

print()
print("Displaying numbers from 0 to 9 which are not divisible by 3")
for j in range(10):
    if j % 3 != 0:
        print(j, end = " | ")

print()
print("Displaying numbers from 0 to 9 which are not divisible by 3 using continue statement")
for j in range(10):
    if j % 3 == 0:
        continue
    print(j, end = " | ")

print()
print("Displaying numbers from 0 to 5 using break statement")
for j in range(10):
    if j == 6:
        break
    print(j, end = " | ")