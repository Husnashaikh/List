# Write a Python program to get the smallest number from a list
# a=[12,13,14,10,3,6,3,57]
# print(min(a))

a=[[1,4,7],[3,6,8]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
