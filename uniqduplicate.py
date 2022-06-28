a=[1,2,3,2,4,1,5,2,6,8,2,4,1,8,2]
i=0
b=[]
c=[]
while i<len(a):
    if i not in a:
        b.append(a[i])
    else:
        c.append(a[i])
    i=i+1
# print(b)
print(c)