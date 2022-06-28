l=[1,2,3,4,5,6,7,8,9,10]
i=0
b=[]
while i<len(l):
    if l[i]%2==0:
        b.append(l[i])
    i=i+1
print(b)
