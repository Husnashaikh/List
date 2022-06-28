
a=[12,34,21,12113]
i=0
sum=0 
b=[]
while i<len(a):
    c=len(a)
    d=a[i]
    j=0
    while j<(c):
        sum=sum+d
        j=j+1
        b.append(sum)
        i=i+1
print(b)
