l=[2,1,0]
print("Raw list:", l)
for i in range(0,len(l)):                     
    for j in range(0,len(l)-1):               
        if (l[j]>l[j+1]):
            temp=l[j]
            l[j], l[j+1] = l[j+1], l[j]
print("Sorted List:", l)