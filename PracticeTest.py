raw_list : list[int | str | float] = [3, 4, 5, 6, 7, "Rahul", 3.45]
size_raw_list : int = len(raw_list)
reversed_list : list[int] = []*len(raw_list)
index : int = 0
for value in range(len(raw_list)-1, -1, -1):
    reversed_list[index] = raw_list[value]
    index += 1
print("Reversed List:", reversed_list)
