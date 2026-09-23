# for loop

data = [2, 'Navin', 4.5, 8, 'Telusko', 'Python']

print('Accessing data using while loop:')
i = 0
while i < len(data):
    print(data[i], end = " | ")
    i += 1

print()
print("Accesing data using for loop:")
for value in data:
    print(value, end = " | ")

print()
print("Displaying numbers from 0 to 9:")
for j in range(10):
    print(j, end = " | ")
