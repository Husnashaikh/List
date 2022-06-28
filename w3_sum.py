# Write a Python program to sum all the items in a list. 
from itertools import count


a=[12,13,14,10,3,6,3,57]
i=0
sum=0
while i<len(a):
    sum=sum+a[i]
    i=i+1
print(sum)