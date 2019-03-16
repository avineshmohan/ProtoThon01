import math 

value = input('Enter the values')

mylist = value.split(",")
n = len(mylist)
for i in range (n):
    mylist[i] = float(mylist[i])
for i in range (n):
    mylist[i] *= mylist[i]

    
    mean = sum(mylist)/float(n)
    
    
    root = math.sqrt(mean)
    
print(root)