# Write a Python program to get the largest number from a list.
a=[12,13,14,10,3,6,3,57]
i=0
b=0
while i<len(a):
    if a[i]>b:
        b=a[i]
    i=i+1
print(b)