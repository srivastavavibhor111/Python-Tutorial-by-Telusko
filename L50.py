# Operator overloading

a = 5
b = 6
# c = a + b

c = int.__add__(a,b)
d = a.__add__(b)

print(c)
print(d)

# print(a)
print(a.__str__())


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} : {self.balance}'

    def __add__(self, other):
        return Account('combined', self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance
    

user1 = Account('navin', 1000)
user2 = Account('kiran', 2000)

combined = user1 + user2

print(user1)
print(user2)
print(combined)

if user1 > user2:
    print("Navin pays the bill")
else:
    print("Kiran pays the bill")


# Homework
class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __str__(self):
        return f"{self.name} : {self.points}"

    def __add__(self, other):
        return Score("Total", self.points + other.points)

    def __lt__(self, other):
        return self.points < other.points

p1 = Score("Player1",  40)
p2 = Score("Player2", 60)

combined = p1 + p2

print(p1)
print(p2)
print(combined)

if p1 < p2:
    print("Player2 wins!")
else:
    print("Player1 wins!")